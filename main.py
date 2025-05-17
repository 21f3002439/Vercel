from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks once on startup
with open("students.json", "r") as f:
    data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    result = []
    for n in name:
        result.append(data.get(n, None))
    return {"marks": result}
