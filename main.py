from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins and methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load students data on startup safely
data = {}

try:
    with open("q-vercel-python.json", "r") as f:
        students_list = json.load(f)
        # Convert list of dicts to dict for fast lookup
        data = {entry["name"]: entry["marks"] for entry in students_list}
except FileNotFoundError:
    print("Warning: q-vercel-python.json file not found. Starting with empty data.")
except json.JSONDecodeError as e:
    print(f"Warning: Error decoding JSON: {e}. Starting with empty data.")

@app.get("/api")
def get_marks(name: list[str] = []):
    if not data:
        raise HTTPException(status_code=404, detail="Students data not available")

    result = [data.get(n) for n in name]
    return {"marks": result}
