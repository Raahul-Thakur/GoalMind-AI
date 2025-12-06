Core modules at a glance
Folder	Purpose
pipelines/	Fetch live football data nightly and store it
ml/	Predict future points + generate optimal transfers
llm/	Reasoning and natural-language decision making
database/	PostgreSQL + Vector DB handling
dashboard/	UI for visual analytics
backend/	FastAPI endpoints for production apps
app.py	MVP UI (Streamlit)


User → asks: “Who to captain this week?”
                   │
                   ▼
          llm_engine.py (understands request)
                   │
                   ▼
         rag_retriever.py (pulls latest stats)
                   │
                   ▼
  ml/captaincy_booster.py (Bayesian scoring)
                   │
                   ▼
  prompt_templates/captaincy.txt (reasoning format)
                   │
                   ▼
      Final answer + justification + stats visual


Example MVP features per UI page
Page	Output
Team View	Shows your XI, xGI trends, EO risk
Captain Picker	Recommends captain with reasoning
Player Compare	Compare 2–3 players by stats & fixtures
Transfer Advisor	Suggest top 5 transfer paths
Rotation Planner	Bench boost / defense rotations

APIs = raw source
DB = storage + structure
Feature builder = intelligence generator
ML = prediction engine
LLM with RAG = reasoning engine
UI = user experience

API's to use
API	Cost	Notes
Official FPL API	FREE	Unlimited — no key needed
Understat API	FREE	Unofficial — scraping/wrapper but reliable
FBRef (scrape / StatBomb tables)	FREE	No auth, just polite-rate scraping
FPL Price Change predictors (FPLStatistics / FPLReview scrape)	FREE	No official API → scrape JSON endpoints
SofaScore / FotMob unofficial API Technically free No official public key; scrape safely