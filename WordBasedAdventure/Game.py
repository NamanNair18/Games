# Define the rooms and their connections
rooms = {
    'hallway': {
        'description': 'You are in a dusty hallway of a haunted house. Shadows flicker on the walls. Doors lead north, east, and west.',
        'north': 'library',
        'east': 'kitchen',
        'west': 'living_room'
    },
        'library': {
        'description': 'You are in a library filled with ancient books. A single dusty tome stands out on a shelf.',
        'south': 'hallway'
    },
        'kitchen': {
        'description': 'You are in a creaky kitchen. A faded mat lies on the floor, slightly askew.',
        'west': 'hallway'
    },
        'living_room': {
        'description': 'You are in a living room with peeling wallpaper. A heavy door to the south is locked.',
        'east': 'hallway',
        'south': 'bedroom'  # Accessible only after unlocking
    },
        'bedroom': {
        'description': 'You are in a bedroom with cobwebs in the corners. A cracked window offers a way out.',
        'north': 'living_room'
    }
}
# Initialize game state
current_room = 'hallway'
inventory = []
door_unlocked = False
key_revealed = False

# Game loop
print("Welcome to the Haunted House Adventure! Type 'quit' to exit.")
while True:
    # Display current room info
    print("\n" + rooms[current_room]['description'])
    if current_room == 'kitchen' and key_revealed:
        print("There is a rusty key on the floor.")

    # Show possible directions
    directions = [d for d in rooms[current_room] if d != 'description']
    print("You can go:", ', '.join(directions))
    print("Inventory:", inventory or "empty")

        # Get player input
    command = input("What do you want to do? ").lower().split()
    if not command:
        continue

    action = command[0]

        # Handle commands
    if action == 'quit':
        print("Thanks for playing!")
        break
    elif action == 'go' and len(command) > 1:
        direction = command[1]
        if direction in rooms[current_room]:
            if current_room == 'living_room' and direction == 'south' and not door_unlocked:
                print("The door is locked. You need a key.")
            else:
                current_room = rooms[current_room][direction]
                print("You move to the", current_room + ".")
        else:
            print("You can't go that way!")
    elif action == 'look':
        print(rooms[current_room]['description'])

    elif action == 'take' and len(command) > 1:
        item = command[1]
        if current_room == 'kitchen' and item == 'key' and key_revealed:
            inventory.append('key')
            key_revealed = False
            print("You pick up the rusty key.")
        else:
            print("There's no such item here.")
    elif action == 'use' and len(command) > 1:
        item = command[1]
        if current_room == 'living_room' and item == 'key' and 'key' in inventory:
            door_unlocked = True
            inventory.remove('key')
            print("You unlock the door with the key.")
        else:
            print("You can't use that here.")
    elif action == 'read' and current_room == 'library':
        print("You open the tome. It reads: 'The key lies beneath the mat.'")

    elif action == 'look' and current_room == 'kitchen' and 'under' in command and 'mat' in command:
        if not key_revealed:
            key_revealed = True
            print("You lift the mat and find a rusty key underneath.")
        else:
            print("There's nothing else under the mat.")

