
# ==========================================
# Assignment: Hands-on - First Python Programs
# Project: My First Python Program
# Description: Collect and display user details
# using variables, input/output and type casting.
# ==========================================


# Step 1: Display program introduction

print("=" * 50)
print("           MY FIRST PYTHON PROGRAM")
print("=" * 50)

print("\nWelcome! Let's create your personal profile.\n")


# Step 2: Accept user details using input()

name = input("Enter your name: ")

# Convert age input from string to integer
age = int(input("Enter your age: "))

# Convert height input from string to float
height = float(input("Enter your height in meters: "))

# Accept favorite number and convert it to float
favorite_number = float(input("Enter your favorite number: "))


# Step 3: Display formatted user information

print("\n" + "=" * 50)
print("              USER PROFILE")
print("=" * 50)

print(f"Name             : {name}")
print(f"Age              : {age} years")
print(f"Height           : {height:.2f} meters")
print(f"Favorite Number  : {favorite_number:g}")

print("=" * 50)


# Step 4: Display data types using type()

print("\n--- DATA TYPE INFORMATION ---")

print("Name Type:", type(name))
print("Age Type:", type(age))
print("Height Type:", type(height))
print("Favorite Number Type:", type(favorite_number))


# Step 5: Perform arithmetic operations

# Add the user's age and favorite number
total = age + favorite_number

print("\n--- ARITHMETIC OPERATION ---")

print(f"Age: {age}")
print(f"Favorite Number: {favorite_number:g}")
print(f"Sum of Age and Favorite Number: {total:g}")


# Step 6: Display final message

print("\nThank you for using My First Python Program!")
print("Program executed successfully.")
print("=" * 50)
