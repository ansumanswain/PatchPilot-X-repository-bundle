from fastapi import FastAPI
from pydantic import BaseModel
from agents.orchestrator import PatchPilot

app = FastAPI()

class TaskRequest(BaseModel):
    task: str
    repo_path: str
    target_file: str

@app.post("/run")
def run(request: TaskRequest):
    pilot = PatchPilot(
        request.repo_path,
        request.target_file,
    )

    pilot.run(request.task)

    return {"status": "completed"}
