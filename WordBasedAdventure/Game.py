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