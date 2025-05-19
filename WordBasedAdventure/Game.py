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
