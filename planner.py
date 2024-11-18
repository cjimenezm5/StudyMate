import os
import json
# Store objects in JSON files as assignments in an array
def load_from_JSON(filename):
    filepath = "Data/" + filename + ".json"

    if not os.path.exists("Data/" + filename + ".json"):
        print(f"File '{"Data/" + filename + ".json"}' does not exist.")
        return []

    try:
        
        with open("Data/" + filename + ".json", "r") as f:
            return json.load(f)  
    except json.JSONDecodeError:
        print(f"Error: The file '{"Data/" + filename + ".json"}' contains invalid JSON.")
        return []