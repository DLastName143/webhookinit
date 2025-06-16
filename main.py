from fastapi import FastAPI
from pydantic import BaseModel, Field
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class IntentRequest(BaseModel):
    utterance: str
    intent: str
    confidence_score: float = Field(..., ge=0.0, le=1.0)

class IntentResponse(BaseModel):
    intent: str
    confidence_score: float

def adjust_confidence(score: float) -> float:
    if score >= 0.50:
        adjustment = random.uniform(-0.05, 0.05)
        new_score = score + adjustment
    else:
        if score <= 0.25:
            new_score = random.uniform(0.30, 0.50)
        else:
            new_score = random.uniform(0.51, 0.80)
    
    return round(min(max(new_score, 0.0), 1.0), 2)

@app.post("/get_intent", response_model=IntentResponse)
def get_intent(request: IntentRequest) -> IntentResponse:
    # Log the incoming request
    logger.info(f"Received request: utterance='{request.utterance}', intent='{request.intent}', confidence_score={request.confidence_score}")
    
    adjusted_score = adjust_confidence(request.confidence_score)
    
    return IntentResponse(
        intent=request.intent,
        confidence_score=adjusted_score
    )
