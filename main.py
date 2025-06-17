from fastapi import FastAPI
from pydantic import BaseModel, Field
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Define incoming request and response models
class IntentRequest(BaseModel):
    utterance: str
    intent: str
    confidence_score: float = Field(..., ge=0.0, le=1.0)

class IntentResponse(BaseModel):
    intent: str
    confidence_score: float

def get_random_intent_and_confidence(score: float) -> tuple:
    # Randomly choose between 'refunds' and 'atmDispute'
    intent = random.choice(["refunds", "atmDispute"])

    # Adjust confidence score based on the selected intent
    if intent == "refunds":
        adjustment = random.uniform(0.51, 0.90)  # Adjust between 5% and 20%
        new_score = score + adjustment
    elif intent == "atmDispute":
        adjustment = random.uniform(0.51, 0.88)  # Adjust between -10% and 10%
        new_score = score + adjustment
    
    # Ensure the score stays between 0.0 and 1.0
    return intent, round(min(max(new_score, 0.0), 1.0), 2)

@app.post("/get_intent", response_model=IntentResponse)
def get_intent(request: IntentRequest) -> IntentResponse:
    logger.info(f"Received request: utterance='{request.utterance}', intent='{request.intent}', confidence_score={request.confidence_score}")
    
    # Get a random intent (either 'refunds' or 'atmDispute') and the adjusted confidence score
    adjusted_intent, adjusted_score = get_random_intent_and_confidence(request.confidence_score)
    
    return IntentResponse(
        intent=adjusted_intent,
        confidence_score=adjusted_score
    )
