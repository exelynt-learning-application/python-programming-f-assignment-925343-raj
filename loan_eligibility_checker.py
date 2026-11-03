
# ==========================================
# Assignment: Nested Conditions
# Project: Loan Eligibility Checker
# Description: Checks loan eligibility based
#              on the applicant's age and salary.
# ==========================================

# Step 1: Display program title

print("=" * 45)
print("        LOAN ELIGIBILITY CHECKER")
print("=" * 45)


# Step 2: Accept applicant details

try:
    age = int(input("\nEnter your age: "))
    salary = float(input("Enter your monthly salary (Rs.): "))

    # Step 3: Validate the input values

    if age <= 0 or salary < 0:
        print("\nInvalid Input!")
        print("Please enter a valid age and salary.")

    else:

        # Step 4: Check the minimum age requirement.
        # The outer if block starts here.
        # Applicant must be at least 21 years old.

        if age >= 21:

            print("\nAge Requirement: Satisfied")

            # Step 5: Nested condition.
            # This salary check runs only when
            # the applicant satisfies the age requirement.

            if salary >= 25000:

                print("Salary Requirement: Satisfied")

                # Both conditions are satisfied.
                print("\n" + "=" * 45)
                print("          LOAN ELIGIBILITY RESULT")
                print("=" * 45)

                print("Age:", age)
                print(f"Monthly Salary: Rs. {salary:,.2f}")
                print("Status: ELIGIBLE FOR LOAN")
                print("Reason: Age and salary requirements are met.")

            else:

                # Age is sufficient, but salary is below the limit.
                print("Salary Requirement: Not Satisfied")

                print("\n" + "=" * 45)
                print("          LOAN ELIGIBILITY RESULT")
                print("=" * 45)

                print("Status: NOT ELIGIBLE")
                print("Reason: Monthly salary must be at least Rs. 25,000.")

        else:

            # Outer else block:
            # Applicant does not meet the minimum age requirement.
            print("\n" + "=" * 45)
            print("          LOAN ELIGIBILITY RESULT")
            print("=" * 45)

            print("Status: NOT ELIGIBLE")
            print("Reason: Applicant must be at least 21 years old.")

    # Step 6: Program completion message

    print("\nLoan eligibility check completed.")

except ValueError:
    print("\nInvalid Input!")
    print("Please enter age as a whole number and salary as a number.")

print("=" * 45)
