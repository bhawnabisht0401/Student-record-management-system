
students = {}

def add_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    students[roll_no] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    for roll_no, details in students.items():
        print("\nRoll Number:", roll_no)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Course:", details["course"])
        print("Marks:", details["marks"])


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    if roll_no in students:
        print("Student Details:", students[roll_no])
    else:
        print("Student not found!")


def update_student():
    roll_no = input("Enter Roll Number to update: ")

    if roll_no in students:
        name = input("Enter New Name: ")
        age = int(input("Enter New Age: "))
        course = input("Enter New Course: ")
        marks = float(input("Enter New Marks: "))

        students[roll_no] = {
            "name": name,
            "age": age,
            "course": course,
            "marks": marks
        }

        print("Student record updated!")
    else:
        print("Student not found!")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student record deleted!")
    else:
        print("Student not found!")


while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Thank you for using Student Record System!")
        break
    else:
        print("Invalid choice! Please try again.")
