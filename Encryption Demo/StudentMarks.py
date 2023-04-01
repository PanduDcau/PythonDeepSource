# Program to take student name and marks as input and write the average and total marks into a text file

# # Taking input from user
# name = input("Enter student name: ")
# marks = list(map(int, input("Enter marks of student: ").split()))
#
# # Calculating total and average marks
# total_marks = sum(marks)
# avg_marks = total_marks/len(marks)
#
# # Writing output to a text file
# with open('studentmarks.txt', 'w') as f:
#     f.write("Name: " + name + "\n")
#     f.write("Total Marks: " + str(total_marks) + "\n")
#     f.write("Average Marks: " + str(avg_marks))

# Write the total and average marks to a file with the student's name
with open("Mark2.txt", "w") as f:
    # Store the number of students
    num_students = int(input("Enter the number of students: "))

    # Initialize lists to store student information
    student_names = []
    student_marks = []
    student_average = []

    # Loop through the number of students
    for i in range(num_students):
        # Get the name and marks of each student
        name = input("Enter the name of student %d: " % (i + 1))
        marks = list(map(int, input("Enter marks of student: ").split()))

        # Append the information to the lists
        student_names.append(name)
        total_marks = sum(marks)
        student_marks.append(total_marks)
        average = total_marks / len(marks)
        student_average.append(average)

    # Calculate the total marks and average for each student
    for i in range(num_students):
        # Get the current student information
        name = student_names[i]
        marks = student_marks[i]
        average = student_average[i]
        print(name)

        f.write(str(name) + " " + str(marks) + " " + str(average) + "\n")