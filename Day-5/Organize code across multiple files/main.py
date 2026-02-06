import math_operations

base_input = float(input("Enter the base for power calculation: "))
exp_input = float(input("Enter the exponent: "))
power_result = math_operations.power(base_input, exp_input)
print(f"{base_input}^{exp_input} = {power_result}")

print("\nLet's calculate the average of some numbers!")
how_many = int(input("How many numbers do you want to average? "))

numbers = []
for i in range(how_many):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

avg_result = math_operations.average(numbers)
print(f"The average of {numbers} is: {avg_result}")