from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Input model
class IntentRequest(BaseModel):
    utterance: str
    intent: str
    confidence_score: float

# Output model
class IntentResponse(BaseModel):
    intent: str
    confidence_score: float

@app.post("/get_intent", response_model=IntentResponse)
def get_intent(request: IntentRequest):
    # Just echo back intent and confidence_score
    return IntentResponse(
        intent=request.intent,
        confidence_score=request.confidence_score
    )
