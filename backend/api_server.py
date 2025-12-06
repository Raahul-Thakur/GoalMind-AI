"""FastAPI application that stitches together ML and LLM routers."""

from __future__ import annotations

from fastapi import FastAPI

from backend import router_llm, router_ml

app = FastAPI(title="GoalMind AI API", version="0.1.0")
app.include_router(router_ml.router)
app.include_router(router_llm.router)


@app.get("/health")
def healthcheck():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
