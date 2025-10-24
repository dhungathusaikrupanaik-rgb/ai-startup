# utils/memory.py
import json
from pathlib import Path
from datetime import datetime

MEM_FILE = Path("memory/memory.json")
MEM_FILE.parent.mkdir(parents=True, exist_ok=True)

def save_memory(entry: dict):
    entry_with_ts = {"timestamp": datetime.utcnow().isoformat(), **entry}
    with MEM_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry_with_ts, ensure_ascii=False) + "\n")

def load_memory(limit: int = 100):
    if not MEM_FILE.exists():
        return []
    with MEM_FILE.open("r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()
    lines = [json.loads(l) for l in lines if l.strip()]
    return lines[-limit:]
