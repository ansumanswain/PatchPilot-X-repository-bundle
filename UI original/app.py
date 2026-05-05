import streamlit as st
from agents.orchestrator import PatchPilot

st.set_page_config(page_title="PatchPilot")

st.title("PatchPilot")
st.caption("Autonomous Coding Agent")

repo_path = st.text_input("Repository", "demo_repo")

task = st.text_area(
    "Task",
    "Fix login validation bug when email contains trailing spaces"
)

if st.button("Run Autonomous Agent"):
    pilot = PatchPilot(
        repo_path,
        "demo_repo/app/auth.py"
    )

    pilot.run(task)
