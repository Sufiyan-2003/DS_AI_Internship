screen_res = (1920, 1080)
print("Current Resolution: 1920x1080")

try:
    screen_res[0] = 1280 
    print("Resolution changed successfully!")
except TypeError as e:
    print(f"Error occurred: {e}")
    
print("Tuples cannot be modified!")

print("\n--- Additional Examples ---")

game_settings = ("Fullscreen", 60, "High")
print(f"Game settings (tuple): {game_settings}")
print("Attempting to change tuple...")

try:
    game_settings[1] = 120  
except TypeError as e:
    print(f"Cannot change tuple: {e}")

game_settings_list = ["Fullscreen", 60, "High"]
print(f"\nGame settings (list): {game_settings_list}")
print("Changing list value...")
game_settings_list[1] = 120  
print(f"Game settings after change: {game_settings_list}")
print("Lists can be modified!")

print("\n--- When to Use Tuples ---")
print("1. When data should not change (constants, configurations)")
print("2. For dictionary keys (tuples are hashable, lists are not)")
print("3. When returning multiple values from a function")
print("4. For data integrity - ensuring values don't get accidentally modified")