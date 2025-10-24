# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from agents.ceo import ceo_agents

app = FastAPI()

class Goal(BaseModel):
    goal: str

@app.post("/run")
async def run(goal: Goal):
    result = ceo_agent(goal.goal)
    return result
