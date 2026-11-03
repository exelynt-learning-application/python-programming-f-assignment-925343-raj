
# ==========================================
# Assignment: Input & Output Operations
# Project: Interactive User Profile Program
# ==========================================

# 1. Display program introduction

print("=" * 45)
print("       INTERACTIVE USER PROFILE")
print("=" * 45)

print("\nWelcome! Please enter your details below.")
print("Let's create your personal profile.\n")


# 2. Accept user input

# input() accepts information from the user.
# int() converts age into an integer.
# float() converts course fee into a decimal number.

student_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
email = input("Enter your email address: ")
course_name = input("Enter your course name: ")
course_fee = float(input("Enter your course fee: Rs. "))
city = input("Enter your city: ")


# 3. Accept enrollment status

enrollment_input = input(
    "Are you enrolled? (yes/no): "
).strip().lower()

is_enrolled = enrollment_input == "yes"


# 4. Display formatted user profile

print("\n" + "=" * 45)
print("             STUDENT PROFILE")
print("=" * 45)

print(f"Student Name       : {student_name}")
print(f"Age                : {age}")
print(f"Email Address      : {email}")
print(f"Course Name        : {course_name}")
print(f"Course Fee         : Rs. {course_fee:.2f}")
print(f"City               : {city}")
print(f"Enrollment Status  : {'Enrolled' if is_enrolled else 'Not Enrolled'}")

print("=" * 45)


# 5. Display completion message

print("\nThank you for providing your information!")
print("Your student profile has been generated successfully.")
