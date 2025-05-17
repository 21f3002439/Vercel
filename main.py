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
    data = {item['name']: item['marks'] for item in raw_data}
    print(f"Loaded {len(data)} records from JSON.")
except Exception as e:
    print(f"Error loading JSON: {e}")




@app.get("/api")
def get_marks(name: list[str] = []):
    result = []
    not_found = []
    for n in name:
        marks = data.get(n)
        if marks is None:
            not_found.append(n)
        else:
            result.append(marks)
    return {
        "requested_names": name,
        "marks": result,
        "not_found": not_found,
        "data_loaded_count": len(data)
    }


import os

@app.get("/debug-file")
def debug_file():
    exists = os.path.isfile("q-vercel-python.json")
    return {"q-vercel-python.json exists": exists}
