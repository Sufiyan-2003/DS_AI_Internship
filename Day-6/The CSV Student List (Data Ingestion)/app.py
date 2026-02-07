import csv

# 1. Create the CSV file with exact data from instructions
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Grade", "Status"])
    writer.writerow(["Alice", "A", "Pass"])
    writer.writerow(["Bob", "B", "Pass"])
    writer.writerow(["Charlie", "F", "Fail"])

print("CSV file created with data:")
print("Name,Grade,Status")
print("Alice,A,Pass")
print("Bob,B,Pass")
print("Charlie,F,Fail")

print("\n" + "="*40)
print("Students who passed:")
print("-" * 20)

# 2. Read and filter for passed students
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if row["Status"] == "Pass":
            print(f"✓ {row['Name']}")

print("\nOnly students with 'Pass' status are displayed.")