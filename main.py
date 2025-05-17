from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# Enable CORS for all origins and methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data from q-vercel-python.json on startup
data = {}

try:
    with open("q-vercel-python.json", "r") as f:
        raw_data = json.load(f)
    # Convert list of dicts to dictionary {name: marks}
    data = {item['name']: item['marks'] for item in raw_data}
except FileNotFoundError:
    print("Warning: q-vercel-python.json file not found. Starting with empty data.")
except json.JSONDecodeError as e:
    print(f"Warning: Error decoding JSON: {e}. Starting with empty data.")

@app.get("/api")
def get_marks(name: list[str] = []):
    result = [data.get(n) for n in name]
    return {"marks": result}
