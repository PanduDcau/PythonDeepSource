def display_menu():
    print("\nMenu:")
    print("1. Add student record")
    print("2. Display highest total marks")
    print("3. Display least total marks")
    print("4. Display students with average marks >= 50 (Pass)")
    print("5. Display students with average marks < 50 (Fail)")
    print("6. Exit the program")


def add_student_record(students):
    name = input("Enter student name: ")
    math_marks = int(input("Enter Mathematics marks: "))
    english_marks = int(input("Enter English marks: "))
    comp_marks = int(input("Enter Computer marks: "))
    total_marks = math_marks + english_marks + comp_marks
    students.append({
        "name": name,
        "math_marks": math_marks,
        "english_marks": english_marks,
        "comp_marks": comp_marks,
        "total_marks": total_marks
    })
    print(f"Record added for {name}")


def display_highest_total(students):
    if students:
        highest = max(students, key=lambda x: x["total_marks"])
        print(f"Highest total marks: {highest['total_marks']} (Student: {highest['name']})")
    else:
        print("No student records available.")


def display_least_total(students):
    if students:
        least = min(students, key=lambda x: x["total_marks"])
        print(f"Least total marks: {least['total_marks']} (Student: {least['name']})")
    else:
        print("No student records available.")


def display_pass_students(students):
    pass_students = [s for s in students if (s["total_marks"] / 3) >= 50]
    if pass_students:
        print("Students with average marks >= 50 (Pass):")
        for s in pass_students:
            print(f"Name: {s['name']}, Total Marks: {s['total_marks']}")
    else:
        print("No students with average marks >= 50.")


def display_fail_students(students):
    fail_students = [s for s in students if (s["total_marks"] / 3) < 50]
    if fail_students:
        print("Students with average marks < 50 (Fail):")
        for s in fail_students:
            print(f"Name: {s['name']}, Total Marks: {s['total_marks']}")
    else:
        print("No students with average marks < 50.")


def main():
    students = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_student_record(students)
        elif choice == 2:
            display_highest_total(students)
        elif choice == 3:
            display_least_total(students)
        elif choice == 4:
            display_pass_students(students)
        elif choice == 5:
            display_fail_students(students)
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
