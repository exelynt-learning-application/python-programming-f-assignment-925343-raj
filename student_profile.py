
# ==========================================
# Assignment: Variables & Data Types
# Project: Student Profile Generator
# ==========================================

# 1. Store student details using variables

student_name = "Rahul Sharma"  # String
student_age = 21              # Integer
course_fee = 15000.50         # Float
is_enrolled = True            # Boolean


# 2. Display original student profile

print("===================================")
print("       STUDENT PROFILE")
print("===================================")

print("Student Name:", student_name)
print("Student Age:", student_age)
print("Course Fee: Rs.", course_fee)
print("Enrollment Status:", is_enrolled)


# 3. Display data types using type()

print("\n--- ORIGINAL DATA TYPES ---")

print("Name Type:", type(student_name))
print("Age Type:", type(student_age))
print("Course Fee Type:", type(course_fee))
print("Enrollment Type:", type(is_enrolled))


# 4. Update student details dynamically

print("\n--- UPDATING STUDENT DETAILS ---")

# Increment student age by 1
student_age = student_age + 1

# Update enrollment status
is_enrolled = False

# Demonstrate dynamic typing:
# Initially course_fee is a float.
# Now update it with a string value.
course_fee_note = course_fee
course_fee_note = "Fee calculation completed"


# 5. Perform a fee calculation

tax_percentage = 5.0

tax_amount = course_fee * tax_percentage / 100
updated_course_fee = course_fee + tax_amount


# 6. Display updated student profile

print("\n--- UPDATED STUDENT PROFILE ---")

print("Student Name:", student_name)
print("Updated Age:", student_age)
print("Original Course Fee: Rs.", course_fee)
print("Tax Amount (5%): Rs.", tax_amount)
print("Updated Course Fee: Rs.", updated_course_fee)
print("Enrollment Status:", is_enrolled)
print("Fee Note:", course_fee_note)


# 7. Display updated data types

print("\n--- UPDATED DATA TYPES ---")

print("Name Type:", type(student_name))
print("Age Type:", type(student_age))
print("Course Fee Type:", type(updated_course_fee))
print("Enrollment Type:", type(is_enrolled))
print("Fee Note Type:", type(course_fee_note))


# 8. Program completion message

print("\nStudent profile generated successfully!")
print("===================================")
