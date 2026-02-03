print("=== Profile Card Generator ===")

item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
in_stock_input = input("Is it in stock? (yes/no): ")

in_stock = in_stock_input.lower() == "yes"

total_cost = quantity * price

print("\n=== Receipt ===")
print("Item:", item_name, ", Qty:", quantity, ", Price:", price, ", Available:", in_stock)

print("Total Cost:", total_cost)