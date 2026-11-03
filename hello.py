
# ==================================================
# Project: Hello World Python Program
# Assignment: Week 1 Final Test
# Description: Demonstrates Python basics, variables,
#              user input, and formatted output.
# ==================================================


# Step 1: Display Hello World message

print("=" * 50)
print("          HELLO WORLD - PYTHON")
print("=" * 50)

print("\nHello, World!")
print("Welcome to Python Programming!")


# Step 2: Store user information using variables

# input() accepts information from the user.
# Each input is stored in a separate variable.

name = input("\nEnter your name: ")

age = int(input("Enter your age: "))

city = input("Enter your city: ")


# Step 3: Display user information

# f-strings are used to display variable values
# in a readable and formatted manner.

print("\n" + "=" * 50)
print("              USER INFORMATION")
print("=" * 50)

print(f"Name : {name}")
print(f"Age  : {age} years")
print(f"City : {city}")


# Step 4: Display a personalized welcome message

print("\nHello", name + "!")
print(f"Welcome to Python Programming from {city}.")

# Step 5: Display program completion message

print("\nProgram executed successfully!")
print("=" * 50)
