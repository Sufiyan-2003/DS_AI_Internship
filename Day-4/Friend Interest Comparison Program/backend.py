print("=== Friend Interest Analyzer ===\n")

friend_a = set()
friend_b = set()

print("Enter interests for Friend A (enter 'done' to finish):")
while True:
    interest = input("Interest: ").strip()
    
    if interest.lower() == 'done':
        break
    
    if interest:
        friend_a.add(interest)

print("\nEnter interests for Friend B (enter 'done' to finish):")
while True:
    interest = input("Interest: ").strip()
    
    if interest.lower() == 'done':
        break
    
    if interest:
        friend_b.add(interest)

print("\n" + "="*50)

print("FRIEND A'S INTERESTS:")
print(friend_a)
print(f"\nFRIEND B'S INTERESTS:")
print(friend_b)

print("\n" + "="*50)
print("INTEREST ANALYSIS RESULTS:\n")

common_interests = friend_a & friend_b
print("1. COMMON INTERESTS (things they both like):")
if common_interests:
    for interest in common_interests:
        print(f"   • {interest}")
else:
    print("   No common interests found")

all_interests = friend_a | friend_b
print(f"\n2. ALL INTERESTS ({len(all_interests)} total unique interests):")
if all_interests:
    for interest in all_interests:
        print(f"   • {interest}")
else:
    print("   No interests entered")

a_unique = friend_a - friend_b
print(f"\n3. FRIEND A'S UNIQUE INTERESTS ({len(a_unique)} interests):")
if a_unique:
    for interest in a_unique:
        print(f"   • {interest}")
else:
    print("   Friend A has no unique interests")

b_unique = friend_b - friend_a
print(f"\n4. FRIEND B'S UNIQUE INTERESTS ({len(b_unique)} interests):")
if b_unique:
    for interest in b_unique:
        print(f"   • {interest}")
else:
    print("   Friend B has no unique interests")

print("\n" + "="*50)
print("SUMMARY:")
print(f"Friend A has {len(friend_a)} interests")
print(f"Friend B has {len(friend_b)} interests")
print(f"They share {len(common_interests)} common interests")
print(f"Total unique interests between them: {len(all_interests)}")
print("="*50)