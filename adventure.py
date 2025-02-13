import random

def acquire_item(inventory, item):
    inventory.append(item)  # Using append() to add an item to the inventory
    print(f"You found a {item} in the room.")
    return inventory

def display_inventory(inventory):
    if not inventory:  # Check if inventory is empty
        print("Your inventory is empty.")
    else:
        print("Your inventory:")
        for i, item in enumerate(inventory, start=1):
            print(f"{i}. {item}")

def enter_dungeon(player_health, inventory, dungeon_rooms):
    for room in dungeon_rooms:
        room_description, item, challenge_type, challenge_outcome = room
        print(f"\n{room_description}")

        # If there's an item in the room, acquire it
        if item:
            inventory = acquire_item(inventory, item)

        # Handle the challenge in the room
        if challenge_type == "puzzle":
            print("You encounter a puzzle!")
            choice = input("Do you want to 'solve' or 'skip' the puzzle? ").strip().lower()
            if choice == "solve":
                success = random.choice([True, False])
                if success:
                    print(challenge_outcome[0])  # Success message
                    player_health += challenge_outcome[2]  # Update health on success
                else:
                    print(challenge_outcome[1])  # Failure message
                    player_health += challenge_outcome[2]  # Update health on failure
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
    # Initial game setup
    player_health = 100
    inventory = []

    # Dungeon setup
    dungeon_rooms = [
        ("A dusty old library", "key", "puzzle", ("You solved the puzzle!", "The puzzle remains unsolved.", -5)),
        ("A narrow passage with a creaky floor", None, "trap", ("You skillfully avoid the trap!", "You triggered a trap!", -10)),
        ("A grand hall with a shimmering pool", "healing potion", "none", None),
        ("A small room with a locked chest", "treasure", "puzzle", ("You cracked the code!", "The chest remains stubbornly locked.", -5))
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
