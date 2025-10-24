# agents/analyst.py
from dashboard.utils.llm import call_model
from dashboard.utils.memory import save_memory

def analyst_agent(task: str, dev_result: dict = None, mkt_result: dict = None):
    combined = f"Developer output:\n{dev_result}\n\nMarketer output:\n{mkt_result}\n\nTask for analyst: {task}"
    prompt = (
        "You are a product analyst. Summarize the current status, risks, and 3 next milestones.\n"
        f"{combined}"
    )
    out = call_model(prompt, system="You are an insightful analyst.", max_tokens=400)
    save_memory({"role":"analyst","task":task,"output":out})
    return {"task":task,"output":out}
