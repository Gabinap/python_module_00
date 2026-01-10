"""
Data Quest - Exercise 4: Inventory Master
This module demonstrates dictionary operations for inventory management.
Manages player inventories with nested dictionaries, calculates inventory
values, handles item transactions, and generates comprehensive reports.

Functions:
    calculate_inventory_value: Calculate total gold value of inventory
    count_items: Count total number of items in inventory
    categorize_items: Group items by their category
    transfer_item: Transfer items between player inventories
    main: Demonstrate inventory system operations

Author:
    gagulhon (@École 42)
Version:
    1.0 (2025-01-05)
"""


def calculate_inventory_value(inventory):
    """
    Calculate the total gold value of an inventory.
    
    Args:
        inventory: Dictionary mapping item names to item details
        
    Returns:
        int: Total gold value of all items
        
    Examples:
        >>> inv = {'sword': {'quantity': 1, 'value': 500}}
        >>> calculate_inventory_value(inv)
        500
    """
    total_value = 0
    for item_details in inventory.values():
        quantity = item_details.get('quantity', 0)
        value = item_details.get('value', 0)
        total_value += quantity * value
    return total_value


def count_items(inventory):
    """
    Count the total number of items in inventory.
    
    Args:
        inventory: Dictionary mapping item names to item details
        
    Returns:
        int: Total count of all items
        
    Examples:
        >>> inv = {'sword': {'quantity': 1}, 'potion': {'quantity': 5}}
        >>> count_items(inv)
        6
    """
    total_items = 0
    for item_details in inventory.values():
        total_items += item_details.get('quantity', 0)
    return total_items


def categorize_items(inventory):
    """
    Group inventory items by their category.
    
    Args:
        inventory: Dictionary mapping item names to item details
        
    Returns:
        dict: Dictionary mapping categories to item counts
        
    Examples:
        >>> inv = {'sword': {'category': 'weapon', 'quantity': 1}}
        >>> categorize_items(inv)
        {'weapon': 1}
    """
    categories = dict()
    for item_details in inventory.values():
        category = item_details.get('category', 'unknown')
        quantity = item_details.get('quantity', 0)
        current_count = categories.get(category, 0)
        categories.update({category: current_count + quantity})
    return categories


def transfer_item(from_inventory, to_inventory, item_name, quantity):
    """
    Transfer items from one inventory to another.
    
    Args:
        from_inventory: Source inventory dictionary
        to_inventory: Destination inventory dictionary
        item_name: Name of item to transfer
        quantity: Number of items to transfer
        
    Returns:
        bool: True if transfer successful, False otherwise
    """
    if item_name not in from_inventory:
        return False
    
    available_quantity = from_inventory[item_name].get('quantity', 0)
    if available_quantity < quantity:
        return False
    
    from_inventory[item_name]['quantity'] -= quantity
    
    if item_name in to_inventory:
        to_inventory[item_name]['quantity'] += quantity
    else:
        new_item = dict()
        for key, value in from_inventory[item_name].items():
            new_item.update({key: value})
        new_item['quantity'] = quantity
        to_inventory.update({item_name: new_item})
    
    return True


def main():
    """
    Demonstrate inventory management system using dictionaries.
    
    Showcases nested dictionaries, value calculations, categorization,
    and item transfers between players.
    
    Returns:
        None: Prints inventory operations directly to stdout
    """
    print("=== Player Inventory System ===")
    print()
    
    alice_inventory = dict({
        'sword': {'quantity': 1, 'value': 500, 'category': 'weapon', 'rarity': 'rare'},
        'potion': {'quantity': 5, 'value': 50, 'category': 'consumable', 'rarity': 'common'},
        'shield': {'quantity': 1, 'value': 200, 'category': 'armor', 'rarity': 'uncommon'}
    })
    
    bob_inventory = dict()
    
    print("=== Alice's Inventory ===")
    for item_name, details in alice_inventory.items():
        quantity = details.get('quantity')
        value = details.get('value')
        category = details.get('category')
        rarity = details.get('rarity')
        item_value = quantity * value
        print(f"{item_name} ({category}, {rarity}): {quantity}x @ {value} gold each = {item_value} gold")
    
    alice_value = calculate_inventory_value(alice_inventory)
    alice_items = count_items(alice_inventory)
    alice_categories = categorize_items(alice_inventory)
    
    print(f"Inventory value: {alice_value} gold")
    print(f"Item count: {alice_items} items")
    
    category_list = []
    for category, count in alice_categories.items():
        category_list.append(f"{category}({count})")
    print(f"Categories: {', '.join(category_list)}")
    print()
    
    print("=== Transaction: Alice gives Bob 2 potions ===")
    success = transfer_item(alice_inventory, bob_inventory, 'potion', 2)
    if success:
        print("Transaction successful!")
    else:
        print("Transaction failed!")
    print()
    
    print("=== Updated Inventories ===")
    alice_potions = alice_inventory.get('potion', dict()).get('quantity', 0)
    bob_potions = bob_inventory.get('potion', dict()).get('quantity', 0)
    print(f"Alice potions: {alice_potions}")
    print(f"Bob potions: {bob_potions}")
    print()
    
    print("=== Inventory Analytics ===")
    
    alice_new_value = calculate_inventory_value(alice_inventory)
    bob_value = calculate_inventory_value(bob_inventory)
    alice_new_items = count_items(alice_inventory)
    bob_items = count_items(bob_inventory)
    
    if alice_new_value > bob_value:
        print(f"Most valuable player: Alice ({alice_new_value} gold)")
    else:
        print(f"Most valuable player: Bob ({bob_value} gold)")
    
    if alice_new_items > bob_items:
        print(f"Most items: Alice ({alice_new_items} items)")
    else:
        print(f"Most items: Bob ({bob_items} items)")
    
    rare_items = []
    for item_name, details in alice_inventory.items():
        if details.get('rarity') == 'rare':
            rare_items.append(item_name)
    
    print(f"Rarest items: {', '.join(rare_items)}")


if __name__ == "__main__":
    main()
