"""
An enhancement of the previous text-based adventure game that implements
an inventory system using lists and incorporating tuples to represent 
fixed game elements.
"""

import random

def acquire_item(inventory, item):
    """
    Adds an item to the player's inventory and prints a message indicating the acquisition.
    
    Args:
        inventory (list): The player's inventory.
        item (str): The item to be added to the inventory.
    
    Returns:
        list: The updated inventory with the new item added.
    """
    inventory.append(item)  # Using append() to add an item to the inventory
    print(f"You acquired a {item}!")
    return inventory

def display_inventory(inventory):
    """
    Displays the contents of the player's inventory. 
    If the inventory is empty, a message is printed.
    
    Args:
        inventory (list): The player's inventory to display.
    """
    if not inventory:  # Check if inventory is empty
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    """
    Simulates a dungeon exploration where the player moves through various rooms,
    acquires items, and faces challenges (puzzles, traps, or no challenge).
    
    Args:
        player_health (int): The player's current health.
        inventory (list): The player's current inventory.
        dungeon_rooms (list): A list of tuples, each representing a room with 
                               its description, item (if any), challenge type, 
                               and challenge outcome.
    
    Returns:
        tuple: A tuple containing the updated player health and inventory after 
               exploring all the rooms in the dungeon.
    """
    for room in dungeon_rooms:
        room_description, item, challenge_type, challenge_outcome = room
        print(f"\n{room_description}")

        # If there's an item in the room, acquire it
        if item:
            print(f"You found a {item} in the room.")  # Add this line to match the test
            inventory = acquire_item(inventory, item)

        # Handle the challenge in the room
        if challenge_type == "puzzle":
            print("You encounter a puzzle!")
            choice = input("Do you want to 'solve' or 'skip' the puzzle? ").strip().lower()
            if choice == "solve":
                success = random.choice([True, False])
                if success:
                    print(challenge_outcome[0])  # Success message
                else:
                    print(challenge_outcome[1])  # Failure message
                player_health += challenge_outcome[2]  # Update health
        elif challenge_type == "trap":
            print("You see a potential trap!")
            choice = input("Do you want to 'disarm' or 'bypass' the trap? ").strip().lower()
            if choice == "disarm":
                success = random.choice([True, False])
                if success:
                    print(challenge_outcome[0])  # Success message
                else:
                    print(challenge_outcome[1])  # Failure message
                    player_health += challenge_outcome[2]  # Update health
        elif challenge_type == "none":
            print("There doesn't seem to be a challenge in this room. You move on.")

        # Ensure player health doesn't drop below zero
        if player_health <= 0:
            player_health = 0
            print("You are barely alive!")

        # Display the updated inventory after each room
        display_inventory(inventory)

    print(f"\nYou exit the dungeon with {player_health} health.")
    return player_health, inventory

def main():
    """
    Main function that sets up the game, initiates the dungeon exploration, 
    and handles combat encounters.
    
    It sets the player's initial health and inventory, defines the dungeon rooms, 
    and simulates a series of challenges. The game ends when the player exits 
    the dungeon or is defeated in combat.
    """
    # Initial game setup
    player_health = 100
    inventory = []

    # Dungeon setup
    dungeon_rooms = [
        ("A dusty old library", "key", "puzzle",
            ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
        ("A narrow passage with a creaky floor", None, "trap",
            ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
        ("A grand hall with a shimmering pool", "healing potion", "none", None),
        ("A small room with a locked chest", "treasure", "puzzle",
            ("You cracked the code!", "The chest remains stubbornly locked.", -5))
    ]

    # Simulate the combat encounter from Week 3 (placeholder logic)
    print("You engage in a combat encounter!")
    combat_success = random.choice([True, False])
    if combat_success:
        print("You survived the combat!")
        player_health -= random.randint(5, 20)  # Simulate health loss from combat
    else:
        print("You were defeated in combat. Game over.")
        return

    # Ensure health is non-negative
    player_health = max(0, player_health)

    # Enter the dungeon if the player survives
    if player_health > 0:
        player_health, inventory = enter_dungeon(player_health, inventory, dungeon_rooms)

    # End of the game
    print(f"Game over. Final health: {player_health}. Final inventory: {inventory}")

if __name__ == "__main__":
    main()
