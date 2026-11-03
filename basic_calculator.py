
# ==========================================
# Assignment: Arithmetic & Assignment Operators
# Project: Basic Calculator Program
# Description: Performs arithmetic and assignment
#              operations on two user-provided numbers.
# ==========================================

# Step 1: Display program title

print("=" * 45)
print("          BASIC CALCULATOR")
print("=" * 45)


# Step 2: Accept two numbers from the user

number1 = float(input("\nEnter the first number: "))
number2 = float(input("Enter the second number: "))


# Step 3: Perform arithmetic operations

print("\n--- ARITHMETIC OPERATIONS ---")

# Addition
addition = number1 + number2
print(f"Addition       : {addition}")

# Subtraction
subtraction = number1 - number2
print(f"Subtraction    : {subtraction}")

# Multiplication
multiplication = number1 * number2
print(f"Multiplication : {multiplication}")

# Division and modulus require a non-zero second number
if number2 != 0:
    division = number1 / number2
    modulus = number1 % number2

    print(f"Division       : {division}")
    print(f"Modulus        : {modulus}")
else:
    print("Division       : Cannot divide by zero.")
    print("Modulus        : Cannot calculate modulus by zero.")


# Step 4: Demonstrate assignment operators

print("\n--- ASSIGNMENT OPERATORS ---")

# Create a separate variable for assignment operations
result = number1

# Add number2 to result using +=
result += number2
print(f"After +=       : {result}")

# Subtract number2 using -=
result -= number2
print(f"After -=       : {result}")

# Multiply result by number2 using *=
result *= number2
print(f"After *=       : {result}")


# Step 5: Display completion message

print("\nCalculator operations completed successfully!")
print("=" * 45)
