def get_stock_level(inventory: dict, item: str) -> int:
    """
    Safely retrieves the stock level of a specific item.
    
    Input:
        inventory (dict): The store's inventory dictionary.
        item (str): The name of the product to look up.
    Output:
        int: The quantity in stock, or 0 if the item doesn't exist.
    """
    return inventory.get(item, 0)


def update_stock(inventory: dict, item: str, quantity: int) -> dict:
    """
    Updates the stock of an item, adding it to the system if it doesn't exist.
    Input:
        inventory (dict): The store's inventory dictionary.
        item (str): The product name.
        quantity (int): The amount to add (can be negative for sales).
    Output:
        dict: The updated inventory dictionary.
    """
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity 
    return inventory


def merge_stores_overwrite(store_a: dict, store_b: dict) -> dict:
    """
    Merges two inventories, where Store B's stock overwrites Store A's on overlap.
    Input:
        store_a (dict): First store's inventory.
        store_b (dict): Second store's inventory.
    Output:
        dict: A new merged dictionary.
    """
    return store_a | store_b


def merge_and_sum_inventories(store_a: dict, store_b: dict) -> dict:
    """
    Merges two inventories and calculates the total sum for overlapping items.
    Input:
        store_a (dict): First store's inventory.
        store_b (dict): Second store's inventory.
    Output:
        dict: A new dictionary containing the combined total of both stores.
    """
   
    all_items = set(store_a.keys()) | set(store_b.keys())
    combined_stock = {
        item: store_a.get(item, 0) + store_b.get(item, 0) 
        for item in all_items
    }
    
    return combined_stock


if __name__ == "__main__":
    print("--- In-Memory Inventory Tracker ---\n")
    
    downtown_store = {"Laptops": 12, "Keyboards": 45, "Monitors": 8}
    uptown_store = {"Laptops": 5, "Mice": 30, "Monitors": 12, "Cables": 100}
    
    print("1. Stock Lookup (.get() method):")
    print(f"Downtown Laptops: {get_stock_level(downtown_store, 'Laptops')}")
    print(f"Downtown Webcams (Not in dict): {get_stock_level(downtown_store, 'Webcams')}\n")
    print("2. Updating Stock:")
    update_stock(downtown_store, "Keyboards", -5) 
    update_stock(downtown_store, "Webcams", 10) 
    print(f"Updated Downtown Store: {downtown_store}\n")
    
    print("3. Merging with Update Operator (Store B overwrites A):")
    merged_overwrite = merge_stores_overwrite(downtown_store, uptown_store)
    print(merged_overwrite)
    
    print("\n4. Merging and Summing with Dictionary Comprehensions:")
    total_inventory = merge_and_sum_inventories(downtown_store, uptown_store)
    print(total_inventory)