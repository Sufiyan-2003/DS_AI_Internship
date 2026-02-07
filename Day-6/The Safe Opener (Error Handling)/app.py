filename = input("Enter the filename to read (e.g., config.txt): ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(f"\nFile '{filename}' contents:")
        print("=" * 40)
        print(content)
        print("=" * 40)
        
except FileNotFoundError:
    print(f"\nOops! That file doesn't exist yet.")
    print(f"The file '{filename}' was not found in the current directory.")
    print("Please check the filename and try again.")