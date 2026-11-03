
# ==========================================
# Assignment: Type Casting
# Project: Type Conversion Practice Program
# ==========================================

# 1. Accept two numbers from the user

print("=" * 45)
print("       TYPE CONVERSION PRACTICE")
print("=" * 45)

number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")


# 2. Convert input values into different data types

# Convert both inputs into integers
int_number1 = int(number1)
int_number2 = int(number2)

# Convert both inputs into floating-point numbers
float_number1 = float(number1)
float_number2 = float(number2)


# 3. Display converted values

print("\n--- CONVERTED VALUES ---")

print("First Integer:", int_number1)
print("Second Integer:", int_number2)

print("First Float:", float_number1)
print("Second Float:", float_number2)


# 4. Perform arithmetic operations using integers

print("\n--- INTEGER ARITHMETIC OPERATIONS ---")

print("Addition:", int_number1 + int_number2)
print("Subtraction:", int_number1 - int_number2)
print("Multiplication:", int_number1 * int_number2)

if int_number2 != 0:
    print("Division:", int_number1 / int_number2)
else:
    print("Division: Cannot divide by zero.")


# 5. Perform arithmetic operations using floats

print("\n--- FLOAT ARITHMETIC OPERATIONS ---")

print("Addition:", float_number1 + float_number2)
print("Subtraction:", float_number1 - float_number2)
print("Multiplication:", float_number1 * float_number2)

if float_number2 != 0:
    print("Division:", float_number1 / float_number2)
else:
    print("Division: Cannot divide by zero.")


# 6. Convert a numeric value into a string

converted_string = str(int_number1)

print("\n--- STRING CONVERSION ---")

print("Converted Value:", converted_string)
print("Message: The number " + converted_string + " is now a string.")


# 7. Display data types using type()

print("\n--- DATA TYPE VERIFICATION ---")

print("Original Input 1:", type(number1))
print("Original Input 2:", type(number2))

print("Integer 1:", type(int_number1))
print("Integer 2:", type(int_number2))

print("Float 1:", type(float_number1))
print("Float 2:", type(float_number2))

print("Converted String:", type(converted_string))


# 8. Completion message

print("\nType conversion practice completed successfully!")
print("=" * 45)
