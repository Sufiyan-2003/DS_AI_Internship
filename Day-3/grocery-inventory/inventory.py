class GroceryInventory:
    def __init__(self):
        self.inventory = ["Apples", "Bananas", "Carrots", "Dates"]
        print("Initial inventory created.")
        print(f"Current inventory: {self.inventory}")
    
    def add_item(self, item_name):
        """Add an item to the inventory using append()"""
        if item_name and item_name not in self.inventory:
            self.inventory.append(item_name)
            print(f"Added '{item_name}' to inventory.")
            return True
        else:
            print(f"Item '{item_name}' already exists or is invalid.")
            return False
    
    def remove_item(self, item_name):
        """Remove an item from the inventory using remove()"""
        if item_name in self.inventory:
            self.inventory.remove(item_name)
            print(f"Removed '{item_name}' from inventory.")
            return True
        else:
            print(f"Item '{item_name}' not found in inventory.")
            return False
    
    def sort_inventory(self):
        """Sort inventory alphabetically using sort()"""
        self.inventory.sort()
        print("Inventory sorted alphabetically.")
    
    def get_inventory(self):
        """Return current inventory"""
        return self.inventory
    
    def print_inventory(self):
        """Print current inventory"""
        print(f"Current inventory: {self.inventory}")
    
    def run_demo_scenario(self):
        """Run the exact scenario from the instructions"""
        print("\n=== Running Demo Scenario ===")
        
        print(f"1. Initial inventory: {self.inventory}")
        
        self.inventory.append("Eggs")
        print(f"2. Added 'Eggs': {self.inventory}")
        
        self.inventory.remove("Bananas")
        print(f"3. Removed 'Bananas': {self.inventory}")
        
        self.inventory.sort()
        print(f"4. Sorted inventory: {self.inventory}")
        print("=== Demo Scenario Complete ===")


if __name__ == "__main__":
    print("=== Grocery Inventory System ===\n")
    
    grocery = GroceryInventory()
    
    grocery.run_demo_scenario()
    
    print("\n=== Final Result ===")
    print(f"Final inventory: {grocery.get_inventory()}")