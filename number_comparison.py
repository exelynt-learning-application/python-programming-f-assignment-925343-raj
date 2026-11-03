
# ==========================================
# Assignment: Comparison & Logical Operators
# Project: Number Comparison Program
# Description: Compares two numbers and checks
#              conditions using logical operators.
# ==========================================

# Step 1: Display program title

print("=" * 45)
print("       NUMBER COMPARISON PROGRAM")
print("=" * 45)


# Step 2: Accept two numbers from the user

number1 = float(input("\nEnter the first number: "))
number2 = float(input("Enter the second number: "))


# Step 3: Perform comparison operations

print("\n--- COMPARISON RESULTS ---")

# Check which number is greater
print("Is first number greater? ", number1 > number2)
print("Is second number greater?", number2 > number1)

# Check whether both numbers are equal
print("Are both numbers equal? ", number1 == number2)


# Step 4: Check whether both numbers are positive

print("\n--- POSITIVE NUMBER CHECK ---")

both_positive = number1 > 0 and number2 > 0

print("Are both numbers positive?", both_positive)


# Step 5: Demonstrate logical OR operator

at_least_one_positive = number1 > 0 or number2 > 0

print("Is at least one number positive?", at_least_one_positive)


# Step 6: Demonstrate logical NOT operator

not_equal = not (number1 == number2)

print("Are the numbers not equal?", not_equal)


# Step 7: Additional logical conditions

print("\n--- ADDITIONAL CONDITIONS ---")

# Check whether both numbers are negative
both_negative = number1 < 0 and number2 < 0

print("Are both numbers negative?", both_negative)

# Check whether both numbers are non-zero
both_non_zero = number1 != 0 and number2 != 0

print("Are both numbers non-zero?", both_non_zero)


# Step 8: Display completion message

print("\nComparison program executed successfully!")
print("=" * 45)
