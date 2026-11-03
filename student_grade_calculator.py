
# ==========================================
# Assignment: if, elif, else Statements
# Project: Student Grade Calculator
# Description: Calculates student grades based
#              on marks entered by the user.
# ==========================================

# Step 1: Display program title

print("=" * 45)
print("        STUDENT GRADE CALCULATOR")
print("=" * 45)


# Step 2: Accept marks from the user

try:
    marks = float(input("\nEnter your marks (0-100): "))

    # Step 3: Validate the entered marks

    if marks < 0 or marks > 100:
        print("\nInvalid Marks!")
        print("Please enter marks between 0 and 100.")

    # Step 4: Calculate grade using if, elif and else

    elif marks >= 90:
        grade = "A"
        result = "Excellent Performance"

    elif marks >= 75:
        grade = "B"
        result = "Very Good Performance"

    elif marks >= 60:
        grade = "C"
        result = "Good Performance"

    else:
        grade = "Fail"
        result = "Needs Improvement"

    # Step 5: Display grade if marks are valid

    if 0 <= marks <= 100:
        print("\n" + "=" * 45)
        print("             STUDENT RESULT")
        print("=" * 45)

        print(f"Marks Obtained : {marks:g}")
        print(f"Grade          : {grade}")
        print(f"Result         : {result}")

        print("=" * 45)
        print("Grade calculation completed successfully!")

# Step 6: Handle invalid non-numeric input

except ValueError:
    print("\nInvalid Input!")
    print("Please enter a valid numeric value.")
