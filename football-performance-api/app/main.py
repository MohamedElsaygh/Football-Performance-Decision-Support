from fastapi import FastAPI
from pydantic import BaseModel
from app.model import make_decision

app = FastAPI(title="Football Performance Decision Support API")

class MatchContext(BaseModel):
    minute: int
    score_diff: int
    fatigue_level: float
    possession_trend: float
@app.get("/")
def root():
    return {"message": "Football Performance Decision Support API is running!"}

@app.post("/decision")
def get_decision(context: MatchContext):
    return make_decision(context)
