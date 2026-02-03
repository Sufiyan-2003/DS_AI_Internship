print("=== Age in 2030 Calculator ===")

name = input("Please enter your name: ")

while True:
    age_str = input("Please enter your current age: ")
    try:
        current_age = int(age_str)
        if current_age < 0 or current_age > 120:
            print("Please enter a valid age (0-120).")
            continue
        break
    except ValueError:
        print("Please enter a valid number for age.")

age_in_2030 = current_age + 4

print(f"\nHey {name}, you will be {age_in_2030} years old in 2030!")