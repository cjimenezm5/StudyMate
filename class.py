
class Assignment():
    def __init__(self):
        self.subject = None
        self.name= None
        self.deadline= None
        self.duration= None
        self.weight= None
        self.size= None
        self.group_work= None

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

    return assignment
