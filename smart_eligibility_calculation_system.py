
# ==========================================================
# Assignment: Week 2 Final Test
# Project: Smart Eligibility & Calculation System
# Description: A menu-driven Python application that checks
#              voting eligibility, calculates student grades,
#              and performs basic mathematical operations.
# ==========================================================


# ----------------------------------------------------------
# FUNCTION 1: Check Voting Eligibility
# ----------------------------------------------------------

def check_voting_eligibility():

    print("\n========== VOTING ELIGIBILITY CHECKER ==========")

    try:
        age = int(input("Enter your age: "))

        # Validate age
        if age <= 0:
            print("Invalid age! Please enter a positive age.")

        # Check voting eligibility
        elif age >= 18:
            print("\nVoting Status: ELIGIBLE")
            print("You are eligible to vote.")

        else:
            print("\nVoting Status: NOT ELIGIBLE")
            print(f"You need to wait {18 - age} more year(s) to vote.")

    except ValueError:
        print("Invalid input! Please enter your age as a whole number.")


# ----------------------------------------------------------
# FUNCTION 2: Student Grade Calculator
# ----------------------------------------------------------

def student_grade_calculator():

    print("\n========== STUDENT GRADE CALCULATOR ==========")

    try:
        marks = float(input("Enter your marks (0-100): "))

        # Validate marks
        if marks < 0 or marks > 100:
            print("Invalid marks! Enter marks between 0 and 100.")

        # Assign grade based on marks
        elif marks >= 90:
            grade = "A"
            result = "Excellent Performance"

        elif marks >= 75:
            grade = "B"
            result = "Very Good Performance"

        elif marks >= 60:
            grade = "C"
            result = "Good Performance"

        elif marks >= 40:
            grade = "D"
            result = "Passed"

        else:
            grade = "Fail"
            result = "Needs Improvement"

        # Display result only for valid marks
        if 0 <= marks <= 100:
            print("\n---------- STUDENT RESULT ----------")
            print(f"Marks  : {marks:g}")
            print(f"Grade  : {grade}")
            print(f"Result : {result}")
            print("------------------------------------")

    except ValueError:
        print("Invalid input! Please enter numeric marks.")


# ----------------------------------------------------------
# FUNCTION 3: Simple Calculator
# ----------------------------------------------------------

def simple_calculator():

    print("\n========== SIMPLE CALCULATOR ==========")

    try:
        # Accept two numbers
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        # Display operation menu
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")

        choice = input("Enter your choice (1-5): ").strip()

        # Perform calculation based on user choice
        if choice == "1":

            result = number1 + number2
            print(f"Addition: {number1} + {number2} = {result}")

        elif choice == "2":

            result = number1 - number2
            print(f"Subtraction: {number1} - {number2} = {result}")

        elif choice == "3":

            result = number1 * number2
            print(f"Multiplication: {number1} * {number2} = {result}")

        elif choice == "4":

            # Prevent division by zero
            if number2 != 0:
                result = number1 / number2
                print(f"Division: {number1} / {number2} = {result}")

            else:
                print("Error: Division by zero is not allowed.")

        elif choice == "5":

            # Prevent modulus by zero
            if number2 != 0:
                result = number1 % number2
                print(f"Modulus: {number1} % {number2} = {result}")

            else:
                print("Error: Modulus by zero is not allowed.")

        else:
            print("Invalid operation! Please select between 1 and 5.")

    except ValueError:
        print("Invalid input! Please enter valid numeric values.")


# ----------------------------------------------------------
# MAIN PROGRAM: Menu-Driven System
# ----------------------------------------------------------

def main():

    while True:

        # Display the main menu
        print("\n" + "=" * 50)
        print("       SMART ELIGIBILITY & CALCULATION SYSTEM")
        print("=" * 50)

        print("\n1. Check Voting Eligibility")
        print("2. Student Grade Calculator")
        print("3. Simple Calculator")
        print("4. Exit")

        print("=" * 50)

        # Accept user's menu choice
        choice = input("Enter your choice (1-4): ").strip()

        # Execute the selected operation
        if choice == "1":

            check_voting_eligibility()

        elif choice == "2":

            student_grade_calculator()

        elif choice == "3":

            simple_calculator()

        elif choice == "4":

            print("\nThank you for using the Smart Eligibility &")
            print("Calculation System.")
            print("Program exited successfully.")
            print("=" * 50)

            break

        else:

            print("\nInvalid menu choice!")
            print("Please select an option between 1 and 4.")


# ----------------------------------------------------------
# PROGRAM EXECUTION STARTS HERE
# ----------------------------------------------------------

if __name__ == "__main__":
    main()
