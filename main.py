from fastapi import FastAPI
from pydantic import BaseModel
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Request model: only the utterance
class UtteranceRequest(BaseModel):
    utterance: str

# Response model
class IntentResponse(BaseModel):
    intent: str
    confidence_score: float

def get_random_intent_and_confidence() -> tuple:
    # Random intent
    intent = random.choice(["refunds", "atmDispute"])

    # Always ensure score > 0.51
    if intent == "refunds":
        score = random.uniform(0.65, 0.90)  # high confidence
    else:  # atmDispute
        score = random.uniform(0.52, 0.75)  # still above 0.51, but maybe lower

    return intent, round(score, 2)

@app.post("/get_intent", response_model=IntentResponse)
def get_intent(request: UtteranceRequest) -> IntentResponse:
    logger.info(f"Received utterance: {request.utterance}")
    
    # Normalize input
    normalized_utterance = request.utterance.strip().lower()

    # Special cases: fixed logic for specific utterances
    if normalized_utterance in [
        "how do i turn off my notifications",
        "add a name to flexible saver"
    ]:
        return IntentResponse(
            intent="atmDispute",
            confidence_score=round(random.uniform(0.11, 0.24), 2)
        )
    if normalized_utterance in [
        "aldi is trying to take a double paynent",
        "aldi is trying to take a double paynent credit card"
    ]:
        return IntentResponse(
            intent="atmDispute",
            confidence_score=round(random.uniform(0.75, 0.95), 2)
        )

    # Default case: random intent and confidence
    intent, confidence_score = get_random_intent_and_confidence()
    return IntentResponse(
        intent=intent,
        confidence_score=confidence_score
    )

