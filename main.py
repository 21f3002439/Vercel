from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the marks data once at startup
with open("marks.json") as f:
    data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = []):
    result = []
    for n in name:
        result.append(data.get(n, None))  # Return None if name not found
    return {"marks": result}
