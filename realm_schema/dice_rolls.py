"""Dice rolls schema"""

# 3rd party
from pydantic import BaseModel


class RollSegment(BaseModel):
    raw: str
    negative: bool = False


class ConstantModifier(RollSegment):
    number: int = 0


class DiceRoll(RollSegment):
    dice: int = 0
    faces: int = 0
    extra: str | None = None


class SegmentResult(BaseModel):
    segment: RollSegment
    rolls: list[int] | None = None
    work: str | None = None
    total: int = 0


class RollResults(BaseModel):
    results: list[SegmentResult]
    min: int | None = None
    max: int | None = None


class BatchResults(BaseModel):
    results: list[RollResults]
