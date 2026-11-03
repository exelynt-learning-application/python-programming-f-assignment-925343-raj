
# ==========================================
# Assignment: Real-Life Decision Examples
# Project: Shopping Discount Calculator
# Description: Calculates shopping discounts
#              based on the purchase amount.
# ==========================================

# Step 1: Display program title

print("=" * 45)
print("       SHOPPING DISCOUNT CALCULATOR")
print("=" * 45)


# Step 2: Accept purchase amount from the user

try:
    purchase_amount = float(
        input("\nEnter your total purchase amount (Rs.): ")
    )

    # Step 3: Validate purchase amount

    if purchase_amount < 0:
        print("\nInvalid purchase amount!")
        print("Please enter an amount greater than or equal to zero.")

    else:

        # Step 4: Apply discount using conditional statements

        if purchase_amount >= 5000:
            discount_percentage = 20

        elif purchase_amount >= 3000:
            discount_percentage = 10

        else:
            discount_percentage = 0

        # Step 5: Calculate discount and final payable amount

        discount_amount = (
            purchase_amount * discount_percentage / 100
        )

        final_amount = purchase_amount - discount_amount

        # Step 6: Display shopping bill

        print("\n" + "=" * 45)
        print("              SHOPPING BILL")
        print("=" * 45)

        print(f"Purchase Amount    : Rs. {purchase_amount:,.2f}")
        print(f"Discount Percentage: {discount_percentage}%")
        print(f"Discount Amount    : Rs. {discount_amount:,.2f}")

        print("-" * 45)

        print(f"Final Payable Amount: Rs. {final_amount:,.2f}")

        print("=" * 45)

        print("\nThank you for shopping with us!")

except ValueError:
    print("\nInvalid Input!")
    print("Please enter a valid numeric purchase amount.")
