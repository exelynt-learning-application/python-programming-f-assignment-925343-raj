
# ==================================================
# Assignment: Conditional Logic Practice Set
# Description: Six Python programs demonstrating
#              conditional statements and logic.
# ==================================================


# ==================================================
# PROGRAM 1: Check Even or Odd
# ==================================================

print("\n========== EVEN OR ODD CHECKER ==========")

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an Even number.")
else:
    print(f"{number} is an Odd number.")


# ==================================================
# PROGRAM 2: Check Leap Year
# ==================================================

print("\n========== LEAP YEAR CHECKER ==========")

year = int(input("Enter a year: "))

# A leap year is divisible by 400,
# or divisible by 4 but not divisible by 100.

if year <= 0:
    print("Please enter a valid positive year.")

elif year % 400 == 0:
    print(f"{year} is a Leap Year.")

elif year % 100 == 0:
    print(f"{year} is not a Leap Year.")

elif year % 4 == 0:
    print(f"{year} is a Leap Year.")

else:
    print(f"{year} is not a Leap Year.")


# ==================================================
# PROGRAM 3: Find Largest of Three Numbers
# ==================================================

print("\n========== LARGEST NUMBER FINDER ==========")

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))

if first >= second and first >= third:
    largest = first

elif second >= first and second >= third:
    largest = second

else:
    largest = third

print(f"The largest number is: {largest:g}")


# ==================================================
# PROGRAM 4: Check Positive, Negative or Zero
# ==================================================

print("\n========== NUMBER SIGN CHECKER ==========")

number = float(input("Enter a number: "))

if number > 0:
    print(f"{number:g} is a Positive number.")

elif number < 0:
    print(f"{number:g} is a Negative number.")

else:
    print("The entered number is Zero.")


# ==================================================
# PROGRAM 5: Student Pass or Fail
# ==================================================

print("\n========== STUDENT RESULT CHECKER ==========")

marks = float(input("Enter student marks (0-100): "))

# Validate marks before checking the result.

if marks < 0 or marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")

elif marks >= 40:
    print(f"Marks: {marks:g}")
    print("Result: PASS")
    print("Congratulations! You passed the examination.")

else:
    print(f"Marks: {marks:g}")
    print("Result: FAIL")
    print("Keep practicing and try again.")


# ==================================================
# PROGRAM 6: Driving License Eligibility
# ==================================================

print("\n========== DRIVING LICENSE ELIGIBILITY ==========")

age = int(input("Enter your age: "))

# This exercise uses 18 as the minimum age.
# Actual eligibility depends on vehicle category
# and applicable licensing rules.

if age <= 0:
    print("Please enter a valid age.")

elif age >= 18:
    print("You are eligible to apply for a driving license.")

else:
    print("You are not yet eligible to apply for a driving license.")
    print(f"You need to wait {18 - age} more year(s).")


# ==================================================
# FINAL MESSAGE
# ==================================================

print("\n==========================================")
print("All six conditional logic programs completed!")
print("Thank you for practicing Python.")
print("==========================================")
