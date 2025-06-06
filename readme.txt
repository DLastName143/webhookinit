# 🌀 Intent Recognition FastAPI API

This FastAPI application accepts an utterance, intent, and confidence score via a POST request, and returns the intent and confidence score as the response.

## 🛠 Requirements

- Python 3.7+
- pip

## 📦 Installation

1. **Clone or download this repository**

2. **Create and activate a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


=================
# Login and select your project
oc login ...
oc project your-project

# Apply all configs
oc apply -f openshift/buildconfig.yaml
oc apply -f openshift/deployment.yaml
oc apply -f openshift/service.yaml
oc apply -f openshift/route.yaml

# Start a build manually (initial trigger)
oc start-build fastapi-intent-build

===========
{"utterance": "help me find my iban", "intent": "#accountinfo", "confidence_score": 0.4}
