"""Streamlit MVP for GoalMind AI."""

from __future__ import annotations

import streamlit as st

from dashboard import charts
from database import queries
from llm.llm_engine import synthesize_answer
from ml import captaincy_booster, transfer_optimizer
from utils.formatters import format_transfer_suggestion

st.set_page_config(page_title="GoalMind AI", page_icon="⚽", layout="wide")
st.title("GoalMind AI — Fantasy Premier League Copilot")
st.caption("Live data + ML + lightweight RAG reasoning")

page = st.sidebar.radio(
    "Navigate",
    [
        "Team View",
        "Captain Picker",
        "Player Compare",
        "Transfer Advisor",
        "Rotation Planner",
    ],
)

st.sidebar.markdown(f"**Gameweek:** {queries.gameweek_context()}")

if page == "Team View":
    st.subheader("Your XI snapshot")
    st.table(charts.team_overview())
    st.subheader("Fixture difficulty")
    st.table(charts.fixture_difficulty())
elif page == "Captain Picker":
    st.subheader("Recommended captain")
    candidates = captaincy_booster.score_candidates(limit=3)
    best = candidates[0]
    st.success(f"{best['name']} — score {best['captain_score']}")
    st.write("Backups")
    st.table([{k: v for k, v in c.items() if k in {"name", "captain_score", "team", "position"}} for c in candidates[1:]])
    st.divider()
    question = st.text_input("Ask a question", "Who to captain this week?")
    if st.button("Ask GoalMind"):
        answer = synthesize_answer(question)
        st.write(answer["answer"])
        st.write("Context")
        for chunk in answer["support"]:
            st.code(f"[{chunk['namespace']}] {chunk['text']}")
elif page == "Player Compare":
    st.subheader("Compare players")
    available = [p["name"] for p in queries.get_players()]
    picks = st.multiselect("Choose players", available, default=available[:2])
    if picks:
        data = charts.compare_players(picks)
        st.table(data)
elif page == "Transfer Advisor":
    st.subheader("Top transfer paths")
    moves = transfer_optimizer.suggest_transfers(limit=5)
    st.write("\n".join(format_transfer_suggestion(moves)))
elif page == "Rotation Planner":
    st.subheader("Bench boost & defensive rotation")
    fixtures = charts.fixture_difficulty()
    st.write("Rotate based on lowest FDR this week. Upcoming fixtures:")
    st.table(fixtures)

st.sidebar.info("This MVP uses mock data so you can focus on the experience first.")
