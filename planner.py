import os
import json
import heapq
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


def scheduler(name, weekend_study_hours, weekday_study_hours):
    assignment_list = load_from_JSON(name)

    # Initialize priority queue as an empty heap
    day = 1  # Track the day

    while assignment_list:  # Continue while there are assignments
        print("Day ", day)
        if day % 6 == 0 or day % 7 == 0:
            study_hours = weekend_study_hours
        else:
            study_hours = weekday_study_hours

        # Calculate priorities and populate the queue
        priority_queue = []
        for assignment in assignment_list:
            # Update priority for each assignment
            assignment["priority"] = calculate_priority(assignment, study_hours)
            # Push the assignment into the heap (use name as a unique identifier)
            heapq.heappush(priority_queue, (-assignment["priority"], assignment["name"]))

        # Use all study hours in the day
        for i in range(study_hours):
            if not priority_queue:
                # Refill the queue if it's empty but assignments still exist
                for assignment in assignment_list:
                    assignment["priority"] = calculate_priority(assignment, study_hours)
                    heapq.heappush(priority_queue, (-assignment["priority"], assignment["name"]))

            if priority_queue:
                # Get the highest-priority assignment
                _, assignment_name = heapq.heappop(priority_queue)

                # Find the corresponding assignment object
                current_assignment = next((a for a in assignment_list if a["name"] == assignment_name), None)

                if current_assignment:
                    print(f"Hour {i + 1}: {current_assignment['name']}")
                    current_assignment["real_duration"] -= 1

                    # If the assignment is completed, remove it
                    if current_assignment["real_duration"] == 0:
                        assignment_list.remove(current_assignment)
                    else:
                        # Recalculate priority and re-add to the heap
                        current_assignment["priority"] = calculate_priority(current_assignment, study_hours)
                        heapq.heappush(priority_queue, (-current_assignment["priority"], current_assignment["name"]))

        # Reduce the deadline for all assignments
        for assignment in assignment_list:  # Iterate over a copy to avoid modification issues
            assignment["deadline"] -= 1
            if assignment["deadline"] <= 0:
                print(f"Missed deadline for assignment: {assignment['name']}")
                assignment_list.remove(assignment)

        day += 1
