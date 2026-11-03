
# ==========================================
# Assignment: match-case Statement
# Project: Menu-Based Calculator
# Description: Performs arithmetic operations
#              using Python match-case.
# ==========================================

# Step 1: Display calculator menu

print("=" * 45)
print("         MENU-BASED CALCULATOR")
print("=" * 45)

print("\nSelect an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Step 2: Accept user's choice

choice = input("\nEnter your choice (1-4): ").strip()

# Step 3: Accept two numbers

try:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Step 4: Perform operation using match-case

    print("\n--- CALCULATION RESULT ---")

    match choice:

        case "1":
            result = number1 + number2
            print("Operation: Addition")
            print(f"Result: {number1} + {number2} = {result}")

        case "2":
            result = number1 - number2
            print("Operation: Subtraction")
            print(f"Result: {number1} - {number2} = {result}")

        case "3":
            result = number1 * number2
            print("Operation: Multiplication")
            print(f"Result: {number1} * {number2} = {result}")

        case "4":
            if number2 != 0:
                result = number1 / number2
                print("Operation: Division")
                print(f"Result: {number1} / {number2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")

        case _:
            print("Invalid choice!")
            print("Please select an option between 1 and 4.")

    # Step 5: Display completion message

    print("\nCalculator execution completed.")

except ValueError:
    print("\nInvalid input!")
    print("Please enter valid numeric values.")

print("=" * 45)
