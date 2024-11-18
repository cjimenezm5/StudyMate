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
    
# Study hours = number of hours the student plans in working per day
def calculate_priority(assignment, study_hours):
    remaining_hours = assignment["deadline"] * study_hours
        
    priority = 0  
    
    if assignment["deadline"] < 2:
        priority += 10
    elif assignment["deadline"] < 4:
        priority += 8
    elif assignment["deadline"] < 6:
        priority += 6
    elif assignment["deadline"] < 8:
        priority += 4

    if (remaining_hours - assignment["real_duration"]) < 2:
        priority += 20
    elif (remaining_hours - assignment["real_duration"]) < 4:
        priority += 15
    elif (remaining_hours - assignment["real_duration"]) < 6:
        priority += 10

    if assignment["weight"] > 20:
        priority += 6
    elif assignment["weight"] > 15:
        priority += 4
    elif assignment["weight"] > 10:
        priority += 2

    if assignment["size"] == 1:
        priority += 3
    elif assignment["size"] == 2:
        priority += 2
    elif assignment["size"] == 3:
        priority += 1

    return priority


def scheduler(name, study_hours):
    assignment_list = load_from_JSON(name)

    # Initializing priority queue
    priority_queue = []
    day = 1  # Track the day
    while assignment_list:  # Continue while there are assignments
        print("Day ", day)
        for i in range(study_hours):
            priority_queue = []

            # Calculate priorities and populate the queue
            for assignment in assignment_list:
                assignment["priority"] = calculate_priority(assignment, study_hours)
                priority_queue.append(assignment)

            # Sort the queue based on priority
            priority_queue.sort(key=lambda x: x["priority"], reverse=True)

            # Select the highest-priority assignment
            if priority_queue:
                current_assignment = priority_queue[0]
                print("Hour ", i + 1, ": ", current_assignment["name"])
                current_assignment["real_duration"] -= 1

                # Remove completed assignment
                if current_assignment["real_duration"] == 0:
                    assignment_list.remove(current_assignment)

        # Reduce the deadline for all assignments
        for assignment in assignment_list:  # Use a copy to avoid modifying the list during iteration
            assignment["deadline"] -= 1
            if assignment["deadline"] == 0:
                assignment_list.remove(assignment)

        day += 1