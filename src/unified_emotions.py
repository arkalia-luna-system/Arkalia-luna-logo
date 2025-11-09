"""
🌙 Unified Emotions Module
Mapping unifié entre émotions BBIA Reachy Sim et variantes Arkalia-LUNA
Préparé pour intégration future avec /Volumes/T7/bbia-reachy-sim/
"""

from typing import Dict, List, Optional

from .variants import VariantType


class UnifiedEmotions:
    """Mapping unifié des émotions entre BBIA Reachy Sim et Arkalia-LUNA"""

    # Mapping BBIA → Arkalia-LUNA
    BBIA_TO_ARKALIA: Dict[str, VariantType] = {
        # Émotions SDK officiel (6)
        "neutral": VariantType.SERENITY,  # Neutre → Sérénité
        "happy": VariantType.CREATIVE,  # Joie → Créatif
        "sad": VariantType.RAINY,  # Tristesse → Pluie
        "angry": VariantType.STORMY,  # Colère → Orage
        "surprised": VariantType.AWAKENING,  # Surprise → Éveil
        "excited": VariantType.EXPLOSIVE,  # Excitation → Explosif
        # Émotions étendues (6)
        "calm": VariantType.SERENITY,  # Calme → Sérénité
        "curious": VariantType.MYSTERY,  # Curiosité → Mystère
        "sleepy": VariantType.SNOWY,  # Somnolence → Neige
        "playful": VariantType.CREATIVE,  # Joueur → Créatif
        "focused": VariantType.POWER,  # Concentration → Puissance
        "confused": VariantType.MYSTERY,  # Confusion → Mystère
    }

    # Mapping inverse Arkalia-LUNA → BBIA
    ARKALIA_TO_BBIA: Dict[VariantType, List[str]] = {
        VariantType.SERENITY: ["neutral", "calm"],
        VariantType.POWER: ["focused"],
        VariantType.MYSTERY: ["curious", "confused"],
        VariantType.AWAKENING: ["surprised"],
        VariantType.CREATIVE: ["happy", "playful"],
        VariantType.RAINY: ["sad"],
        VariantType.STORMY: ["angry"],
        VariantType.EXPLOSIVE: ["excited"],
        VariantType.SUNNY: ["happy", "excited"],  # Approximation
        VariantType.SNOWY: ["sleepy"],
    }

    @classmethod
    def bbia_to_arkalia(cls, bbia_emotion: str) -> Optional[VariantType]:
        """Convertit une émotion BBIA en variante Arkalia-LUNA"""
        return cls.BBIA_TO_ARKALIA.get(bbia_emotion.lower())

    @classmethod
    def arkalia_to_bbia(cls, arkalia_variant: VariantType) -> List[str]:
        """Convertit une variante Arkalia-LUNA en liste d'émotions BBIA"""
        return cls.ARKALIA_TO_BBIA.get(arkalia_variant, [])

    @classmethod
    def get_all_bbia_emotions(cls) -> List[str]:
        """Retourne toutes les émotions BBIA disponibles"""
        return list(cls.BBIA_TO_ARKALIA.keys())

    @classmethod
    def get_all_arkalia_variants(cls) -> List[VariantType]:
        """Retourne toutes les variantes Arkalia-LUNA disponibles"""
        return list(set(cls.BBIA_TO_ARKALIA.values()))

    @classmethod
    def is_valid_bbia_emotion(cls, emotion: str) -> bool:
        """Vérifie si une émotion BBIA est valide"""
        return emotion.lower() in cls.BBIA_TO_ARKALIA

    @classmethod
    def get_mapping_stats(cls) -> Dict[str, int]:
        """Retourne les statistiques du mapping"""
        return {
            "bbia_emotions": len(cls.BBIA_TO_ARKALIA),
            "arkalia_variants": len(cls.get_all_arkalia_variants()),
            "mappings": len(cls.BBIA_TO_ARKALIA),
        }


# Instance globale
UNIFIED_EMOTIONS = UnifiedEmotions()
