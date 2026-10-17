total = 0.0

print("===== EXPENSE TRACKER =====")
print("Enter your expense amounts one by one.")
print("Type 'done' when you have finished.")

while True:
    user_input = input("Enter expense amount: ")

    if user_input.lower() == "done":
        break

    try:
        amount = float(user_input)

        if amount < 0:
            print("Expense cannot be negative.")
            continue

        total = total + amount
        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid number or type 'done'.")

print("---------------------------")
print(f"Total Spent: Rs. {total:.2f}")
print("Thank you for using Expense Tracker!")
