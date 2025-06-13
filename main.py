from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class IntentRequest(BaseModel):
    utterance: str
    intent: str
    confidence_score: float

class IntentResponse(BaseModel):
    intent: str
    confidence_score: float

def adjust_confidence(score: float) -> float:
    if score >= 0.50:
        # Small realistic adjustment ±0.05
        adjustment = random.uniform(-0.05, 0.05)
        new_score = score + adjustment
    else:
        # Conditional random replacement
        if score <= 0.25:
            # Stay low if input is very low
            new_score = random.uniform(0.30, 0.50)
        else:
            # Score is low but not too low, assign moderate random
            new_score = random.uniform(0.30, 0.80)
    
    return round(min(max(new_score, 0.0), 1.0), 2)

@app.post("/get_intent", response_model=IntentResponse)
def get_intent(request: IntentRequest) -> IntentResponse:
    adjusted_score = adjust_confidence(request.confidence_score)
    return IntentResponse(
        custom_intent=request.intent,
        confidence_score=adjusted_score
    )
