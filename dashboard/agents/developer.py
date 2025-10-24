# agents/developer.py
from dashboard.utils.llm import call_model
from dashboard.utils.memory import save_memory

def developer_agent(task: str):
    prompt = (
        f"You are a pragmatic developer. Given this task, produce:\n"
        "1) One-paragraph architecture summary.\n"
        "2) Files to create (filename + short content outline).\n"
        "3) A starter code snippet for the main module.\n\n"
        f"Task: {task}\nReturn clearly labeled sections."
    )
    out = call_model(prompt, system="You are a helpful senior developer.", max_tokens=700)
    save_memory({"role":"developer","task":task,"output":out})
    return {"task":task,"output":out}
