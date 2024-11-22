import json
import class1
import planner
import displayfunctions
import os

def main():
    name = str(input("Enter your name: "))
    
    # Check if the user is a new user by checking if a file with their name exists
    try:
        with open("Data/" + name + ".json", "r") as f:
            print("Welcome back", name)
    except FileNotFoundError:
        # Create a new user file
        with open("Data/" + name + ".json", "w") as f:
            print("Welcome", name)
            f.write("[]")
    
    # Main menu
    while True:
        print("\nOptions:")
        print("1. Add an assignment")
        print("2. Delete an assignment")
        print("3. Create schedule")
        print("4. Display assignments")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            assignment = class1.create_assignment()
            class1.load_to_JSON(name, assignment)
        elif choice == "2":
            assignment_name = str(input("Enter the name of the assignment: "))
            class1.delete_assignment(name, assignment_name)
        elif choice == "3":
            weekday_study_hours = int(input("Enter the number of hours you plan to study per day during the week: "))
            weekend_study_hours = int(input("Enter the number of hours you plan to study per day on weekends: "))
            planner.scheduler(name, weekend_study_hours, weekday_study_hours)
        elif choice == "4":
            displayfunctions.display_menu(name)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()