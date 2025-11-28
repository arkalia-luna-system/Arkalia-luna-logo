"""
🔄 AI Generation Queue System
Système de queue asynchrone pour génération IA
"""

import json
import logging
from dataclasses import asdict, dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

try:
    import redis  # type: ignore[import-untyped]
except ImportError:
    redis = None  # type: ignore[assignment]


class JobStatus(str, Enum):
    """Statut d'un job de génération IA"""

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class AIJob:
    """Job de génération IA"""

    job_id: str
    variant_name: str
    size: int
    generator_type: str
    status: JobStatus
    created_at: str
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
    result_path: Optional[str] = None
    error: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convertit en dictionnaire"""
        data = asdict(self)
        data["status"] = self.status.value
        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AIJob":
        """Crée depuis un dictionnaire"""
        data["status"] = JobStatus(data["status"])
        return cls(**data)


class AIQueueManager:
    """
    Gestionnaire de queue pour génération IA asynchrone
    """

    def __init__(
        self,
        redis_host: str = "localhost",
        redis_port: int = 6379,
        redis_db: int = 0,
    ) -> None:
        """
        Initialise le gestionnaire de queue

        Args:
            redis_host: Host Redis
            redis_port: Port Redis
            redis_db: DB Redis
        """
        self.logger = logging.getLogger(__name__)
        self.redis_client: Optional[redis.Redis] = None
        self.queue_name = "ai_generation_queue"
        self.jobs_prefix = "ai_job:"

        if redis and os.getenv("REDIS_ENABLED", "false").lower() == "true":
            try:
                self.redis_client = redis.Redis(
                    host=redis_host, port=redis_port, db=redis_db, decode_responses=True
                )
                self.redis_client.ping()
                self.logger.info("✅ Queue IA connectée à Redis")
            except redis.exceptions.ConnectionError as e:
                self.logger.warning(f"❌ Redis indisponible pour queue: {e}")
                self.redis_client = None
        else:
            self.logger.info("⚠️ Queue IA en mode mémoire (Redis désactivé)")

        # Queue en mémoire si Redis indisponible
        self._memory_queue: List[AIJob] = []
        self._processing_jobs: Dict[str, AIJob] = {}

    def add_job(
        self,
        variant_name: str,
        size: int,
        generator_type: str = "ai",
    ) -> str:
        """
        Ajoute un job à la queue

        Args:
            variant_name: Nom de la variante
            size: Taille du logo
            generator_type: Type de générateur

        Returns:
            ID du job
        """
        import uuid

        job_id = str(uuid.uuid4())
        job = AIJob(
            job_id=job_id,
            variant_name=variant_name,
            size=size,
            generator_type=generator_type,
            status=JobStatus.PENDING,
            created_at=datetime.now().isoformat(),
        )

        if self.redis_client:
            try:
                # Ajouter à la queue Redis
                self.redis_client.lpush(self.queue_name, json.dumps(job.to_dict()))
                # Stocker le job
                self.redis_client.set(
                    f"{self.jobs_prefix}{job_id}",
                    json.dumps(job.to_dict()),
                    ex=86400,  # 24h
                )
            except Exception as e:
                self.logger.error(f"Erreur ajout job Redis: {e}")
                self._memory_queue.append(job)
        else:
            self._memory_queue.append(job)

        self.logger.info(f"📥 Job {job_id} ajouté à la queue")
        return job_id

    def get_job(self, job_id: str) -> Optional[AIJob]:
        """
        Récupère un job par son ID

        Args:
            job_id: ID du job

        Returns:
            Job ou None
        """
        if self.redis_client:
            try:
                data = self.redis_client.get(f"{self.jobs_prefix}{job_id}")
                if data:
                    return AIJob.from_dict(json.loads(data))
            except Exception as e:
                self.logger.error(f"Erreur récupération job Redis: {e}")

        # Chercher dans la queue mémoire
        for job in self._memory_queue + list(self._processing_jobs.values()):
            if job.job_id == job_id:
                return job

        return None

    def get_next_job(self) -> Optional[AIJob]:
        """
        Récupère le prochain job en attente

        Returns:
            Job ou None
        """
        if self.redis_client:
            try:
                data = self.redis_client.rpop(self.queue_name)
                if data:
                    return AIJob.from_dict(json.loads(data))
            except Exception as e:
                self.logger.error(f"Erreur récupération job Redis: {e}")

        # Chercher dans la queue mémoire
        for job in self._memory_queue:
            if job.status == JobStatus.PENDING:
                self._memory_queue.remove(job)
                return job

        return None

    def update_job_status(
        self,
        job_id: str,
        status: JobStatus,
        result_path: Optional[str] = None,
        error: Optional[str] = None,
    ) -> None:
        """
        Met à jour le statut d'un job

        Args:
            job_id: ID du job
            status: Nouveau statut
            result_path: Chemin du résultat
            error: Message d'erreur
        """
        job = self.get_job(job_id)
        if not job:
            return

        job.status = status
        if status == JobStatus.PROCESSING:
            job.started_at = datetime.now().isoformat()
        elif status == JobStatus.COMPLETED:
            job.completed_at = datetime.now().isoformat()
            job.result_path = result_path
        elif status == JobStatus.FAILED:
            job.completed_at = datetime.now().isoformat()
            job.error = error

        if self.redis_client:
            try:
                self.redis_client.set(
                    f"{self.jobs_prefix}{job_id}",
                    json.dumps(job.to_dict()),
                    ex=86400,
                )
            except Exception as e:
                self.logger.error(f"Erreur mise à jour job Redis: {e}")

        self._processing_jobs[job_id] = job

    def get_queue_size(self) -> int:
        """
        Retourne la taille de la queue

        Returns:
            Nombre de jobs en attente
        """
        if self.redis_client:
            try:
                return self.redis_client.llen(self.queue_name)
            except Exception:
                pass

        return len([j for j in self._memory_queue if j.status == JobStatus.PENDING])

    def get_job_status(self, job_id: str) -> Optional[JobStatus]:
        """
        Récupère le statut d'un job

        Args:
            job_id: ID du job

        Returns:
            Statut ou None
        """
        job = self.get_job(job_id)
        return job.status if job else None


# Import os pour REDIS_ENABLED
import os  # noqa: E402
