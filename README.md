# 🗺️ AI Travel Agent

Welcome to your AI-powered travel planning assistant!  
Plan trips, get weather updates, convert currencies, search places — all in one smart workflow.

---

## 🧰 Available Tools

- **Currency Converter** — Convert between currencies in real-time.
- **Calculator** — Perform quick travel budget calculations.
- **Weather Tool** — Get live weather forecasts for destinations.
- **Place Search Tool**
  - Google Place Search
  - Tavily Place Search

---

## 📸 Workflow Visuals

Below are the visual representations of your trip planning workflow:

![Workflow Image 1](./UI%20images/1.png)  
![Workflow Image 1](./UI%20images/2.png)  
![Workflow Image 1](./UI%20images/3.png)  
![Workflow Image 2](./UI%20images/4.png)  

---

## ⚙️ Architecture

- **Frontend:** [Streamlit](https://streamlit.io/) — user interface for interacting with the AI agent.
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) — handles API requests and invokes the AI workflow.

---

## 🗂️ Project Setup

### ✅ Create & activate a virtual environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🔑 Required API Keys
```Create a .env file or use your environment variables to store these keys:```
```bash
TAVILY_API_KEY=your_tavily_key_here
GPLACES_API_KEY=your_google_places_key_here
GOOGLE_API_KEY=your_google_key_here
OPENAI_API_KEY=your_openai_key_here
ALPHAAVANTAGE_API_KEY=your_alpha_vantage_key_here
EXCHANGE_RATE_API_KEY=your_exchange_rate_key_here
GROQ_API_KEY=your_groq_key_here
```

```python
# Run Fast api backend
uvicorn app:app --reload --port 8000

#Streamit ui run
streamlit run app.py
```
---



# Future Work:

## ✅ **Planned Agent Tools**

- ✈️ **Flight Search** — Find and compare flights for the best deals.
- 🗣️ **Translator Tool** — Translate phrases to assist international travelers.
- 🛡️ **Travel Safety Alerts** — Notify users about travel advisories or local risks.
- 🍽️ **Food Recommendations** — Suggest local cuisines and hidden gems.


## ⚙️ **MLOps / LLMOps Tools**
 | Tool | Purpose |
|------|---------|
| 🗃️ **MLflow** | Experiment tracking, model registry |
| 🐋 **Docker** | Containerized, portable environments |
| 🔁 **CI/CD** | Automated testing & deployment pipelines |
| 🔍 **LangSmith** | LLM chain tracing and evaluation |
| 📊 **Weights & Biases (W&B)** | Visual experiment tracking and monitoring |
| 🗂️ **Prompt Layer** | Version and monitor LLM prompts |
| 🛡️ **Guardrails AI** | Validate and safeguard LLM outputs |
| ☁️ **AWS Lambda** | Serverless tasks like sending emails or alerts |
| 📈 **Prometheus + Grafana** | Metrics collection and system monitoring dashboards |



1) Use a database (PostgreSQL, DynamoDB, or MongoDB) to  store past searches & preferences.
2) Add conversational memory: let the agent remember context during the trip planning session.
3) Add OAuth or sign-in with Google
4) Add a simple feedback button for the user to rate recommendations


5) Instead of just building tools separately, integrate them into a real user flow:
The user inputs their preferences (budget, destination, dates)
The agent searches flights, hotels, weather, attractions and creates a daily itinerary.