"""
Tests pour le système de queue IA
"""

from unittest.mock import patch

import pytest

from src.ai_queue import AIJob, AIQueueManager, JobStatus


class TestAIQueueManager:
    """Tests pour AIQueueManager"""

    @pytest.fixture
    def queue_manager(self) -> AIQueueManager:
        """Créer un gestionnaire de queue"""
        with patch("src.ai_queue.redis"):
            with patch("src.ai_queue.os.getenv", return_value="false"):
                return AIQueueManager()

    def test_queue_manager_init(self, queue_manager: AIQueueManager) -> None:
        """Test initialisation du gestionnaire de queue"""
        assert queue_manager.queue_name == "ai_generation_queue"
        assert queue_manager.redis_client is None

    def test_add_job(self, queue_manager: AIQueueManager) -> None:
        """Test ajout d'un job"""
        job_id = queue_manager.add_job(
            variant_name="serenity",
            size=512,
            generator_type="ai",
        )
        assert job_id is not None
        assert len(job_id) > 0

    def test_get_job(self, queue_manager: AIQueueManager) -> None:
        """Test récupération d'un job"""
        job_id = queue_manager.add_job("serenity", 512)
        job = queue_manager.get_job(job_id)
        assert job is not None
        assert job.variant_name == "serenity"
        assert job.size == 512
        assert job.status == JobStatus.PENDING

    def test_get_next_job(self, queue_manager: AIQueueManager) -> None:
        """Test récupération du prochain job"""
        job_id = queue_manager.add_job("serenity", 512)
        next_job = queue_manager.get_next_job()
        assert next_job is not None
        assert next_job.job_id == job_id

    def test_update_job_status(self, queue_manager: AIQueueManager) -> None:
        """Test mise à jour du statut d'un job"""
        job_id = queue_manager.add_job("serenity", 512)
        queue_manager.update_job_status(job_id, JobStatus.PROCESSING)
        job = queue_manager.get_job(job_id)
        assert job is not None
        assert job.status == JobStatus.PROCESSING

    def test_get_queue_size(self, queue_manager: AIQueueManager) -> None:
        """Test taille de la queue"""
        assert queue_manager.get_queue_size() == 0
        queue_manager.add_job("serenity", 512)
        assert queue_manager.get_queue_size() == 1

    def test_get_job_status(self, queue_manager: AIQueueManager) -> None:
        """Test récupération du statut d'un job"""
        job_id = queue_manager.add_job("serenity", 512)
        status = queue_manager.get_job_status(job_id)
        assert status == JobStatus.PENDING


class TestAIJob:
    """Tests pour AIJob"""

    def test_job_to_dict(self) -> None:
        """Test conversion job en dictionnaire"""
        job = AIJob(
            job_id="test-id",
            variant_name="serenity",
            size=512,
            generator_type="ai",
            status=JobStatus.PENDING,
            created_at="2025-11-28T10:00:00",
        )
        data = job.to_dict()
        assert data["job_id"] == "test-id"
        assert data["status"] == "pending"

    def test_job_from_dict(self) -> None:
        """Test création job depuis dictionnaire"""
        data = {
            "job_id": "test-id",
            "variant_name": "serenity",
            "size": 512,
            "generator_type": "ai",
            "status": "pending",
            "created_at": "2025-11-28T10:00:00",
        }
        job = AIJob.from_dict(data)
        assert job.job_id == "test-id"
        assert job.status == JobStatus.PENDING
