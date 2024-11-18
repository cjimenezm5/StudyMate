import planner
import os
import json

class Assignment():
    def __init__(self):
        self.subject = None
        self.name= None
        self.deadline= None
        self.duration= 1
        self.weight= None
        self.size= 1
        self.group_work= None
        self.priority = None
        self.real_duration = int(self.duration / self.group_size)

    def display(self):
        print("Subject: ", self.subject)
        print("Name: ", self.name)
        print("Deadline: ", self.deadline)
        print("Duration: ", self.duration)
        print("Weight: ", self.weight)
        print("Size: ", self.size)
        print("Group Work: ", self.group_work)

def create_assignment():
    subject = str(input("Enter the name of your subject in capital letters: "))
    name = str(input("Enter the name of your assignment: "))
    deadline = int(input("Enter the number of days until the deadline of your assignment: "))
    duration = int(input("Enter the duration of your assignment in hours (round up): "))
    weight = float(input("Enter the weight of your assignment as a percentage of your grade: "))
    size = int(input("Enter the size of the assignment- big(1), medium(2), small(3): "))
    groupwork = str(input("Is your assignment group work? (yes/no): "))

    assignment = Assignment()
    assignment.subject = subject
    assignment.name = name
    assignment.deadline = deadline
    assignment.duration = duration
    assignment.weight = weight
    assignment.size = size
    if groupwork == "yes":
      assignment.group_work = True
    else:
      assignment.group_work = False
    assignment.real_duration = int(assignment.duration / assignment.group_size)
    return assignment


def load_to_JSON(filename, assignment):
    new_data = {
        "subject": assignment.subject,
        "name": assignment.name,
        "deadline": assignment.deadline,
        "duration": assignment.duration,
        "weight": assignment.weight,
        "size": assignment.size,
        "group_work": assignment.group_work,
        "group_size": assignment.group_size,
        "real_duration": assignment.real_duration,
    }


    if os.path.exists("Data/"+filename+ ".json"):
        with open("Data/"+filename+ ".json", "r") as f:
            try:
                existing_data = json.load(f)
                if not isinstance(existing_data, list):  
                    existing_data = [existing_data]
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    existing_data.append(new_data)
    with open("Data/"+filename+ ".json", "w") as f:
        json.dump(existing_data, f, indent=4)
      
#Delete assignment by loading from Json, deleting the assignment and then writing the new list to the file
def delete_assignment(filename, assignment):
    array = planner.load_from_JSON(filename)
    for i in range(len(array)):
        if array[i].name == assignment.name:
            del array[i]
            break
    with open("Data/"+filename+ ".json", "w") as f:
        for assignment in array:
            load_to_JSON(filename, assignment)