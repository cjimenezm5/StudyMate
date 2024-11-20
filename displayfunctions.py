import planner

def display_all_assignments(assignment_list):
    
    print("\nAll Assignments:")
    for assignment in assignment_list:
        print(
            f"Subject: {assignment['subject']}\n, Name: {assignment['name']}\n, "
            f"Deadline: {assignment['deadline']} days\n, Duration: {assignment['duration']} hours\n, "
            f"Weight: {assignment['weight']}%\n, Group Work: {'Yes' if assignment['group_work'] else 'No'}\n"
        )


def display_assignments_by_subject(assignment_list, subject):

    print(f"\nAssignments for Subject: {subject}")
    filtered = [a for a in assignment_list if a["subject"].lower() == subject.lower()]
    if filtered:
        for assignment in filtered:
            print(
                f"Name: {assignment['name']}\n, Deadline: {assignment['deadline']} days\n, "
                f"Duration: {assignment['duration']} hours\n, Weight: {assignment['weight']}%\n"
            )
    else:
        print(f"No assignments found for subject: {subject}")


def display_assignments_by_shortest_deadline(assignment_list):

    print("\nAssignments by Shortest Deadline:")
    sorted_list = sorted(assignment_list, key=lambda a: a["deadline"])
    for assignment in sorted_list:
        print(
            f"Subject: {assignment['subject']}\n, Name: {assignment['name']}\n, "
            f"Deadline: {assignment['deadline']} days\n, Duration: {assignment['duration']} hours\n"
        )


def display_assignments_by_biggest_duration(assignment_list):

    print("\nAssignments by Biggest Duration:")
    sorted_list = sorted(assignment_list, key=lambda a: a["duration"], reverse=True)
    for assignment in sorted_list:
        print(
            f"Subject: {assignment['subject']}\n, Name: {assignment['name']}\n, "
            f"Duration: {assignment['duration']} hours\n, Deadline: {assignment['deadline']} days\n"
        )

def display_menu(name):
    assignment_list = planner.load_from_JSON(name)
    if not assignment_list:
        print("No assignments found.")
        return

    while True:
        print("\nDisplay Options:")
        print("1. Display all assignments")
        print("2. Display assignments by subject")
        print("3. Display assignments by shortest deadline")
        print("4. Display assignments by biggest duration")
        print("5. Go back")

        choice = input("Enter your choice: ")
        if choice == "1":
            display_all_assignments(assignment_list)
        elif choice == "2":
            subject = input("Enter the subject: ")
            display_assignments_by_subject(assignment_list, subject)
        elif choice == "3":
            display_assignments_by_shortest_deadline(assignment_list)
        elif choice == "4":
            display_assignments_by_biggest_duration(assignment_list)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
