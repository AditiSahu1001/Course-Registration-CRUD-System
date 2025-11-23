import csv
import os

COURSE_FILE = "courses.csv"

def check_course_file():
    if not os.path.exists(COURSE_FILE):
        f = open(COURSE_FILE, "w", newline="")
        w = csv.writer(f)
        w.writerow(["id", "name", "duration", "fees"])
        f.close()

def add_course():
    check_course_file()
    cid = input("Course ID: ")

    f = open(COURSE_FILE, "r")
    rd = csv.DictReader(f)
    for row in rd:
        if row["id"] == cid:
            print("This Course ID already exists.")
            f.close()
            return
    f.close()

    name = input("Course Name: ")
    dur = input("Duration: ")
    fees = input("Fees: ")

    f = open(COURSE_FILE, "a", newline="")
    w = csv.writer(f)
    w.writerow([cid, name, dur, fees])
    f.close()

    print("Course added.")

def view_courses():
    check_course_file()
    print("\n--- Course List ---")

    f = open(COURSE_FILE, "r")
    rd = csv.DictReader(f)
    for row in rd:
        print(row)
    f.close()

def search_course():
    check_course_file()
    cid = input("Course ID to search: ")

    f = open(COURSE_FILE, "r")
    rd = csv.DictReader(f)
    for row in rd:
        if row["id"] == cid:
            print("Found:", row)
            f.close()
            return
    f.close()
    print("Course not found.")

def update_course():
    check_course_file()
    cid = input("Course ID to update: ")

    f = open(COURSE_FILE, "r")
    rd = csv.DictReader(f)
    newrows = []
    found = False

    for row in rd:
        if row["id"] == cid:
            found = True
            print("Press Enter to keep old value.")
            name = input(f"Name ({row['name']}): ") or row["name"]
            dur = input(f"Duration ({row['duration']}): ") or row["duration"]
            fees = input(f"Fees ({row['fees']}): ") or row["fees"]
            newrows.append({"id": cid, "name": name, "duration": dur, "fees": fees})
        else:
            newrows.append(row)
    f.close()

    if not found:
        print("Course ID not found.")
        return

    f = open(COURSE_FILE, "w", newline="")
    w = csv.DictWriter(f, fieldnames=["id", "name", "duration", "fees"])
    w.writeheader()
    w.writerows(newrows)
    f.close()

    print("Course updated.")

def delete_course():
    check_course_file()
    cid = input("Course ID to delete: ")

    f = open(COURSE_FILE, "r")
    rd = csv.DictReader(f)
    newrows = []
    found = False

    for row in rd:
        if row["id"] == cid:
            found = True
        else:
            newrows.append(row)
    f.close()

    if not found:
        print("Course ID not found.")
        return

    f = open(COURSE_FILE, "w", newline="")
    w = csv.DictWriter(f, fieldnames=["id", "name", "duration", "fees"])
    w.writeheader()
    w.writerows(newrows)
    f.close()

    print("Course deleted.")


def course_menu():
    while True:
        print("\n=== COURSE MENU ===")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Search Course")
        print("4. Update Course")
        print("5. Delete Course")
        print("6. Back")

        ch = input("Choose: ")

        if ch == "1":
            add_course()
        elif ch == "2":
            view_courses()
        elif ch == "3":
            search_course()
        elif ch == "4":
            update_course()
        elif ch == "5":
            delete_course()
        elif ch == "6":
            break
        else:
            print("Invalid.")
