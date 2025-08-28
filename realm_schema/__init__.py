"""Shared Realm TTRPG schema"""

from .bot_guilds import BotGuildsResponse
from .dice_rolls import (
    BatchResults,
    ConstantModifier,
    DiceRoll,
    RollResults,
    RollSegment,
    SegmentResult,
)

__all__ = (
    "BatchResults",
    "BotGuildsResponse",
    "ConstantModifier",
    "DiceRoll",
    "RollResults",
    "RollSegment",
    "SegmentResult",
)
