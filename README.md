# Course-Registration-CRUD-System
Course Registration CRUD System is designed to provide a user-Friendly solution for managing academic information. This system allows administrators to add and maintain course details, manage student information, handle student–course enrollments in an organized and structured manner.
The system allows easy management of courses, students, and enrollments through separate modules.
Supports full CRUD operations for adding, viewing, updating, and deleting records.
Uses simple CSV files for storing data, making it lightweight and easy to run anywhere.
Provides a clear menu-driven interface that is easy for beginners to use.
Automatically creates required CSV files if they don’t exist.
Prevents duplicate entries for students, courses, and enrollments.
Shows proper messages for invalid inputs and missing IDs.
The modular code structure makes the system easy to maintain and extend.
Python 3.13 – Used for writing all the program logic and creating the menu-driven application.
CSV Files – Used as the main storage method for courses, students, and enrollments.
IDLE – Used as the code editor for writing and running the Python files.
csv Module – Python’s built-in module for reading and writing CSV data easily.
OS Module – Used to check and create files when required.
1. Install Python
Make sure Python 3.13 is installed on your system.
If not, download it from the official website and install it.
2. Download/Copy the Project Files
Create a new folder anywhere on your computer and place the following files inside it:
main.py
course.py
studet.py
registration.py
You don’t need to manually create CSV files — the program will create them automatically.
3. Open the Project in Your Editor
Use any editor like:
IDLE
VS Code
PyCharm
or even a simple text editor
Open the folder containing the project files.
4. Run the Main File
Open main.py and run it.
You can run it by:
Clicking the Run button in your editor
Or opening Terminal/Command Prompt → navigating to the folder → typing:
python main.py
5. Use the Menu
Once the program starts:
Select Course Management, Student Management, or Registration
Follow the prompts to add, view, update, or delete data
The system will automatically create:
courses.csv
students.csv
enrollments.csv
These will store all your data permanently.
6. Close the Program
Choose the Exit option from the main menu whenever you are done.
Run main.py to open the main menu.

In Course Management, add, view, update, search, and delete a few courses to confirm all operations work.
In Student Management, do the same for student records to check each function.
In Registration, try enrolling a student, viewing enrollments, and removing an enrollment.
Try invalid inputs (wrong IDs, wrong menu numbers) to check error handling.
Restart the program to make sure data is saved properly in the CSV files.
