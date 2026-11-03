
# ==================================================
# Program: Python Syntax and Indentation Demonstration
# Purpose: Demonstrate Python syntax, indentation,
#          conditional statements, and nested blocks.
# ==================================================

# Top-level print statements
print("====================================")
print("     PYTHON SYNTAX DEMONSTRATION")
print("====================================")

print("Welcome to Python Programming!")
print("Learning Python indentation rules.")
print("Understanding conditional statements.")

# Variables
student_name = "Rahul"
marks = 85

print("\nStudent Name:", student_name)
print("Student Marks:", marks)

# Main if block starts here.
# Indentation (4 spaces) is required to define
# which statements belong to this if block.

if marks >= 40:

    print("\nResult: Student has passed.")

    # Nested if block starts here.
    # It is indented further because it is inside
    # the main if block.

    if marks >= 80:
        print("Grade: Excellent")
        print("Performance: Outstanding")

    else:
        print("Grade: Good")
        print("Performance: Keep improving")

    # Nested if-else block ends here when
    # indentation returns to the main if level.

else:
    print("\nResult: Student has failed.")
    print("Please try again.")

# Main if-else block ends here when indentation
# returns to the top-level position.

print("\nProgram execution completed successfully.")
