import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import json
from dashboard.agents.ceo import ceo_agent

# --- App Config ---
st.set_page_config(page_title="AI Multi-Agent Digital Startup", page_icon="🤖")

# --- Title ---
st.title("🚀 AI Multi-Agent Digital Startup System")

# --- Input Section ---
task = st.text_input("💡 Enter your startup idea:")

# --- Placeholder for results ---
result = None

# --- Run Agents Button ---
if st.button("Run Agents"):
    with st.spinner("Agents are working together... 🤖🤝"):
        result = ceo_agent(task)
        st.success("✅ Agents completed their tasks!")
        st.subheader("📊 Results Overview")
        st.json(result)

# --- Download Button (only appears when result exists) ---
if result is not None:
    st.download_button(
        label="📥 Download Full Report",
        data=json.dumps(result, ensure_ascii=False, indent=2),
        file_name="startup_report.json",
        mime="application/json"
    )
st.markdown("---")
st.caption("Powered by your AI Multi-Agent System — Built in Python & Streamlit 💻")

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

LLM_MODE = os.getenv("LLM_MODE")
REMOTE_LLM_URL = os.getenv("REMOTE_LLM_URL")
REMOTE_LLM_KEY = os.getenv("REMOTE_LLM_KEY")

print("🔑 LLM_MODE:", LLM_MODE)
print("🌐 REMOTE_LLM_URL:", REMOTE_LLM_URL)
print("🧠 REMOTE_LLM_KEY loaded:", REMOTE_LLM_KEY is not None)
