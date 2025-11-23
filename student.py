import csv
import os

STUDENT_FILE = "students.csv"

def check_student_file():
    if not os.path.exists(STUDENT_FILE):
        f = open(STUDENT_FILE, "w", newline="")
        w = csv.writer(f)
        w.writerow(["id", "name", "age", "department"])
        f.close()

def add_student():
    check_student_file()
    sid = input("Student ID: ")

    f = open(STUDENT_FILE, "r")
    rd = csv.DictReader(f)
    for row in rd:
        if row["id"] == sid:
            print("Student ID already exists.")
            f.close()
            return
    f.close()

    name = input("Name: ")
    age = input("Age: ")
    dept = input("Department: ")

    f = open(STUDENT_FILE, "a", newline="")
    w = csv.writer(f)
    w.writerow([sid, name, age, dept])
    f.close()

    print("Student added.")

def view_students():
    check_student_file()
    print("\n--- Student List ---")

    f = open(STUDENT_FILE, "r")
    rd = csv.DictReader(f)
    for row in rd:
        print(row)
    f.close()

def search_student():
    check_student_file()
    sid = input("Student ID to search: ")

    f = open(STUDENT_FILE, "r")
    rd = csv.DictReader(f)
    for row in rd:
        if row["id"] == sid:
            print("Found:", row)
            f.close()
            return
    f.close()
    print("Student not found.")

def update_student():
    check_student_file()
    sid = input("Student ID to update: ")

    f = open(STUDENT_FILE, "r")
    rd = csv.DictReader(f)
    newrows = []
    found = False

    for row in rd:
        if row["id"] == sid:
            found = True
            print("Press Enter to keep old values.")
            name = input(f"Name ({row['name']}): ") or row["name"]
            age = input(f"Age ({row['age']}): ") or row["age"]
            dept = input(f"Department ({row['department']}): ") or row["department"]
            newrows.append({"id": sid, "name": name, "age": age, "department": dept})
        else:
            newrows.append(row)
    f.close()

    if not found:
        print("Student ID not found.")
        return

    f = open(STUDENT_FILE, "w", newline="")
    w = csv.DictWriter(f, fieldnames=["id", "name", "age", "department"])
    w.writeheader()
    w.writerows(newrows)
    f.close()

    print("Student updated.")

def delete_student():
    check_student_file()
    sid = input("Student ID to delete: ")

    f = open(STUDENT_FILE, "r")
    rd = csv.DictReader(f)
    newrows = []
    found = False

    for row in rd:
        if row["id"] == sid:
            found = True
        else:
            newrows.append(row)
    f.close()

    if not found:
        print("Student ID not found.")
        return

    f = open(STUDENT_FILE, "w", newline="")
    w = csv.DictWriter(f, fieldnames=["id", "name", "age", "department"])
    w.writeheader()
    w.writerows(newrows)
    f.close()

    print("Student deleted.")

def student_menu():
    while True:
        print("\n=== STUDENT MENU ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back")

        ch = input("Choose: ")

        if ch == "1":
            add_student()
        elif ch == "2":
            view_students()
        elif ch == "3":
            search_student()
        elif ch == "4":
            update_student()
        elif ch == "5":
            delete_student()
        elif ch == "6":
            break
        else:
            print("Invalid.")
