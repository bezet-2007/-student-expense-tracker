expenses = []

while True:
    print("\n--- Student Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category: ")

        expenses.append({
            "item": item,
            "amount": amount,
            "category": category
        })

        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\n--- Expenses ---")
            for expense in expenses:
                print(
                    f"{expense['item']} - "
                    f"₹{expense['amount']:.2f} - "
                    f"{expense['category']}"
                )

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total Expense: ₹{total:.2f}")

    elif choice == "4":
        print("Thank you for using Student Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")
