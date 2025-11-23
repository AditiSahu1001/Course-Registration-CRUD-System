import csv
import os
from student import check_student_file as student_file
from course import check_course_file as course_file

ENROLL_FILE = "enrollments.csv"

def check_enroll_file():
    if not os.path.exists(ENROLL_FILE):
        f = open(ENROLL_FILE, "w", newline="")
        w = csv.writer(f)
        w.writerow(["student_id", "course_id"])
        f.close()

def enroll_student():
    student_file()
    course_file()
    check_enroll_file()

    sid = input("Student ID: ")
    cid = input("Course ID: ")

    f = open(ENROLL_FILE, "r")
    rd = csv.DictReader(f)
    for row in rd:
        if row["student_id"] == sid and row["course_id"] == cid:
            print("Already enrolled.")
            f.close()
            return
    f.close()

    f = open(ENROLL_FILE, "a", newline="")
    w = csv.writer(f)
    w.writerow([sid, cid])
    f.close()

    print("Enrollment done.")

def view_enrollments():
    check_enroll_file()
    print("\n--- Enrollments ---")

    f = open(ENROLL_FILE, "r")
    rd = csv.DictReader(f)
    for row in rd:
        print(row)
    f.close()

def remove_enrollment():
    check_enroll_file()

    sid = input("Student ID: ")
    cid = input("Course ID: ")

    f = open(ENROLL_FILE, "r")
    rd = csv.DictReader(f)
    newrows = []
    found = False

    for row in rd:
        if row["student_id"] == sid and row["course_id"] == cid:
            found = True
        else:
            newrows.append(row)
    f.close()

    if not found:
        print("Enrollment not found.")
        return

    f = open(ENROLL_FILE, "w", newline="")
    w = csv.DictWriter(f, fieldnames=["student_id", "course_id"])
    w.writeheader()
    w.writerows(newrows)
    f.close()

    print("Enrollment removed.")

def registration_menu():
    while True:
        print("\n=== REGISTRATION MENU ===")
        print("1. Enroll Student")
        print("2. View Enrollments")
        print("3. Remove Enrollment")
