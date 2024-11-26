# StudyMate: README Guide

---

## **Description of the App**
Welcome to StudyMate! 🎓✨

StudyMate is a powerful, student-centric tool designed to simplify academic life, minimize stress, and maximize productivity. Built by students, for students, it addresses the challenges we all face, like managing assignments, scheduling study hours, and prioritizing tasks based on deadlines, weight, and duration. Our app will create a personalised schedule with your tasks and will be stored in JSON files for each user enabling to continue with their progress at any time. 

---

## **Features**
StudyMate provides several features to simplify academic planning:

- **Create Assignments**: Users can add detailed assignments, including attributes such as subject, deadline, weight, and group size.
- **Priority-based Scheduling**: The app calculates priority scores for tasks based on factors like urgency, importance, and size, creating an optimized study schedule.
- **Assignment Management**:
  - Save assignments to personalized JSON files for later use.
  - Delete assignments that are no longer relevant.
- **Data Visualization**:
  - View all assignments.
  - Filter and sort assignments by subject, shortest deadline, or largest duration.
- **Customized Study Plans**: Users can input their study hours (weekday and weekend) to receive schedules tailored to their availability.
- **User Profiles**: Each user’s assignments are saved to a separate file for personalized experiences.

---

## **File Structure**
The application is organized into the following files and folders:

### **Python Files**
1. **`main.py`**:
   - Central file for the application.
   - Handles the main program flow and user interactions.
   - Manages options for adding, deleting, displaying, and scheduling assignments.

2. **`class1.py`**:
   - Defines the `Assignment` class.
   - Provides methods for creating, displaying, and saving assignments.
   - Includes logic for handling attributes such as subject, deadline, weight, size, and group work.

3. **`planner.py`**:
   - Implements the scheduling logic.
   - Includes a priority-based scheduler with the use of a priority queuethat allocates study hours to assignments.
   - Handles deadlines and tracks task progress during scheduling.

4. **`displayfunctions.py`**:
   - Includes functions for displaying assignment data.
   - Offers options to view all assignments or filter them by various criteria like subject, deadline, or duration.

### **Data Folder**
- **`Data/`**:
  - Contains JSON files for each user.
  - These files store all user-specific assignment details, enabling a persistent and personalized experience.

---

## **Prerequisites and Environment**
To use StudyMate, ensure your system meets the following requirements:

- **Python Version**: Python 3.7 or higher is required to run the program, make sure it is correctly installed on your system.
- **Operating System**: 
  - The app was developed and tested on various OS to ensure perfect functionality.
- **Required Libraries**:
  - `json`: Used for reading and writing assignment data to JSON files.
  - `os`: For file operations like checking the existence of user files.
  - `heapq`: For implementing priority queues in scheduling logic.

---

## **Installation and Execution**

### **Steps to Get Started**
1. **Download the Repository**:
   - Visit the repository containing StudyMate and download the ZIP file using the dropdown on the green box that says "Code".
   - Extract the ZIP file to a folder of your choice.

2. **Prepare the Environment**:
   - Ensure Python 3.7 or higher is installed. 
   - Double-click on the `main.py` file to launch the program.

3. **Run the Application**:
   - Upon launching, the app will prompt you to enter your name:
     - If you’re a new user, a personalized JSON file will be created in the `Data/` folder.
     - If you’re a returning user, your assignments will be loaded from your existing JSON file and will be received with a "Welcome back".
   - Use the on-screen menu to interact with the app:
     - **Option 1**: Add a new assignment by providing details like subject, deadline, and group size.
     - **Option 2**: Delete an assignment by selecting it from your list.
     - **Option 3**: Generate a daily study schedule based on your study hours.
     - **Option 4**: View your assignments, filtered or sorted as needed.
     - **Option 5**: Exit the application.

---

## **Detailed Execution Walkthrough**

- **Step 1**: Launch `main.py` by double-clicking it and run the code.
- **Step 2**: Enter your name when the program asks.
  - E.g.: Type `María` and press Enter.
- **Step 3**: Follow the menu options:
  - Select `1` to add an assignment.
    - Enter details like subject (`Maths`), deadline (`5 days`), and duration (`4 hours`).
  - Select `2` to delete an assignment.
  - Select `3` to create a study schedule.
    - Specify study hours for weekdays and weekends.
    - View the generated schedule.
  - Select `4` to view your assignments:
    - Choose from filters like subject or deadline.
- **Step 4**: Exit the app with option `5`.

---

## **Further Improvements**
While StudyMate is functional, the following improvements could make it more versatile and user-friendly:
1. **Expand compatibility with external tools**:
   - Connect the app to other tools that students use such as Google Calendar or Blackboard to further sync their tasks and schedules with the app. 
2. **Develop a GUI for the app**:
   - Improve the overall user experience with more visual tools and representations of the app. Hopefully we can bring our mockups to real life nad include elemnts such as timelines, progress bars etc. 
3. **Gamification**:
   - Add features like productivity streaks amnd achievement badges to keep users motivated and on top of their tasks. 
4. **Expand features**:
   - Increase the app's values to  by addressing user needs; add notifications for assignemnts that aer close to the deadline and incorporate other features for group assignments like sharing tasks among group members. 
5. **Improved storage**:
   - Substitute JSON storage system for a database for more efficient storage and data retrieval. 


---

## **Bibliography/Webgraphy**
The following resources were used for the development and understanding of StudyMate:
- [Python Documentation](https://docs.python.org): Comprehensive guide for Python syntax and modules.
- [Heapq Library Documentation](https://docs.python.org/3/library/heapq.html): Information on implementing priority queues.
- [JSON Module Documentation](https://docs.python.org/3/library/json.html): Details on reading and writing JSON data.



