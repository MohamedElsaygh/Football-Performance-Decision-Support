from pydantic import BaseModel

class MatchContext(BaseModel):
    minute: int
    score_diff: int
    fatigue_level: float
    possession_trend: float


class DecisionResponse(BaseModel):
    recommendation: str
    reason: str
    confidence: float
