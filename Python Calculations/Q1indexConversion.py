# Program to show the day of a student based on their registration number
def get_day(reg_number):
    remainder = reg_number % 5
    days = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday"
    }
    return days[remainder]


# Example usage:
registration_number = int(input("Enter registration number: "))
print(f"The student should come on: {get_day(registration_number)}")
