# Get user input for name, age, and student ID
name = input("Enter your name: ")
age = int(input("Enter your age: "))
student_id = input("Enter your student ID: ")

# Get the current year
current_year = 2024

# Calculate the approximate initial birth year
initial_birth_year = current_year - age

# Extract the last four digits of the student ID and convert to an integer
last_four_digits = int(student_id[-4:])

# Adjust the birth year based on the last four digits
adjusted_birth_year = initial_birth_year + last_four_digits if last_four_digits % 2 == 0 else initial_birth_year - last_four_digits

# Print the message with the calculated birth year
print(f"Hello, {name}! Based on the information provided, your initial birth year is {initial_birth_year}.")
print(f"With adjustments, your birth year is approximately {adjusted_birth_year}.")
