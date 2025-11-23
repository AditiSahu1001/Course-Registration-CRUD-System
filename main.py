import course
import student
import registration

def main_menu():
    while True:
        print("\n===== COURSE REGISTRATION SYSTEM =====")
        print("1. Course Management")
        print("2. Student Management")
        print("3. Registration")
        print("4. Exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            course.course_menu()
        elif ch == "2":
            student.student_menu()
        elif ch == "3":
            registration.registration_menu()
        elif ch == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")

main_menu()
