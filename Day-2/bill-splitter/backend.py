print("=== Restaurant Bill Splitter ===")

while True:
    bill_str = input("Enter the total bill amount: ₹")
    try:
        total_bill = float(bill_str)
        if total_bill <= 0:
            print("Bill amount must be greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a valid number (e.g., 45.50).")

while True:
    people_str = input("Enter the number of people: ")
    try:
        num_people = int(people_str)
        if num_people <= 0:
            print("Number of people must be greater than 0.")
            continue
        break
    except ValueError:
        print("Please enter a valid whole number.")

share_per_person = total_bill / num_people

print(f"\n=== Bill Summary ===")
print(f"Total Bill: ₹{total_bill:.2f}")
print(f"Number of People: {num_people}")
print(f"Each person pays: ₹{share_per_person:.2f}")

print(f"\n=== Data Type Verification ===")
print(f"Type of total_bill: {type(total_bill)}")
print(f"Type of num_people: {type(num_people)}")
print(f"Type of share_per_person: {type(share_per_person)}")

print("\nThank you for using the Restaurant Bill Splitter!")