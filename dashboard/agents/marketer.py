# agents/marketer.py
from dashboard.utils.llm import call_model
from dashboard.utils.memory import save_memory

def marketer_agent(task: str):
    prompt = (
        f"You are a growth marketer. Produce:\n"
        "- A 7-day content calendar (channel, topic, short caption)\n"
        "- 3 ready-to-post social captions (Twitter/LinkedIn/Instagram)\n"
        "- A 20-word elevator pitch\n\nTask: {task}"
    )
    out = call_model(prompt, system="You are a data-driven marketer.", max_tokens=600)
    save_memory({"role":"marketer","task":task,"output":out})
    return {"task":task,"output":out}
