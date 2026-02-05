print("=== Unique User ID Analyzer ===\n")

raw_logs = []
print("Enter User IDs from login logs (enter 'done' to finish):")

while True:
    user_id = input("Enter User ID: ").strip()
    
    if user_id.lower() == 'done':
        break
    
    if user_id:  
        raw_logs.append(user_id)

print("\n" + "="*40)

print(f"RAW LOGS LIST ({len(raw_logs)} entries):")
print(raw_logs)

print("\n" + "="*40)
unique_users = set(raw_logs)
print(f"UNIQUE USER SET ({len(unique_users)} unique users):")
print(unique_users)

print("\n" + "="*40)
test_id = input("Enter a User ID to check if it's in the unique set: ").strip()

if test_id in unique_users:
    print(f"✓ '{test_id}' is in the unique set: True")
else:
    print(f"✗ '{test_id}' is not in the unique set: False")

print("\n" + "="*40)
print("COUNT COMPARISON:")
print(f"Original list length: {len(raw_logs)} entries")
print(f"Unique set length: {len(unique_users)} unique users")
print(f"Duplicates removed: {len(raw_logs) - len(unique_users)}")

print("\n" + "="*40)
print("SUMMARY:")
print(f"Total logins: {len(raw_logs)}")
print(f"Unique visitors: {len(unique_users)}")
print("="*40)