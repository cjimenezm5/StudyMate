# StudyMate
Welcome to StudyMate! 🎓✨

StudyMate is a powerful, student-centric tool designed to simplify academic life, minimize stress, and maximize productivity. Built by students, for students, it addresses the challenges we all face, like managing assignments, schedule study hours, and prioritize tasks based on deadlines, weight, and duration. 

**Installation and Execution**

Step 1: Download the Code: Download the ZIP StudyMate-main.zip

Step 2: Install Python or VS Code

Step 3: Unzip the file

Step  4: Open the file StudyMate-main in VS or Python

Step  5: Run main.py

Step 6: Execute the features


# Program File Structure

- **main.py** - Handles program logic and contains the main function.
- **class.py** - Contains the assignment class with all its methods and handles assignment creation.
- **planner.py** - Creates the priority score for scheduling and plans the workweek.
- **displayfunctions.py** - Contains all functions to display assignment information according to user inputs.
- **Data Folder** - The `Data` folder will be in the same directory and will contain JSON files for all users.

---

## main.py

The main file manages all program logic, guiding the user through steps to create their planner. The main function will:

- Prompt for inputs and call corresponding functions based on these inputs.
- Ask for the user’s name and check for an existing JSON file with that name. If none exists, it will create one to store all information.

Since JSON files are written to and read from, there might be a need to create two separate program logic flows:

1. One for creating and deleting assignments.
2. Another for creating the schedule.

The program may need to restart to read new information added to the JSON file.

---

## class.py

This file is dedicated to the `Assignment` class and handles instance creation for each assignment. The class includes the following:

### Attributes

- **Assignment name**
- **Subject**
- **Deadline** (days until due date)
- **Estimated duration** (in hours)
- **Grade weight** (percentage)
- **Assignment size** (small, medium, or big)
- **Group work?**

### Methods

- `__init__` function to initialize attributes.
- **Delete assignment**
- **Display assignment** (basic)
- **Save to JSON**
