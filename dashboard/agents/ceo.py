# agents/ceo.py
from dashboard.utils.llm import call_model
from dashboard.agents.developer import developer_agent
from dashboard.agents.marketer import marketer_agent
from dashboard.agents.analyst import analyst_agent
from dashboard.utils.memory import save_memory

def split_tasks_from_plan(plan_text: str):
    prompt = (
        "You are an assistant that outputs JSON {\"dev\":\"...\",\"mkt\":\"...\",\"ana\":\"...\"}.\n"
        f"Plan: {plan_text}\nReturn the JSON only."
    )
    out = call_model(prompt, system="Return valid JSON only.", max_tokens=300)
    try:
        import json
        return json.loads(out)
    except Exception:
        parts = plan_text.split("\n")
        return {"dev": parts[0] if parts else plan_text, "mkt": parts[1] if len(parts)>1 else "", "ana": parts[2] if len(parts)>2 else ""}

def ceo_agent(goal: str):
    plan_prompt = f"You are CEO. Create a concise plan to achieve: {goal}. List steps and deliverables."
    plan = call_model(plan_prompt, system="You are a strategic CEO.", max_tokens=400)
    save_memory({"role":"ceo","goal":goal,"plan":plan})
    tasks = split_tasks_from_plan(plan)
    dev_out = developer_agent(tasks.get("dev",""))
    mkt_out = marketer_agent(tasks.get("mkt",""))
    ana_out = analyst_agent(tasks.get("ana",""), dev_out, mkt_out)
    result = {"goal": goal, "plan": plan, "dev": dev_out, "mkt": mkt_out, "ana": ana_out}
    save_memory({"role":"ceo_result","result":result})
    return result
