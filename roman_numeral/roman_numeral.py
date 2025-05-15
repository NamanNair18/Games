def roman_to_int(numeral):
     # Dictionary mapping Roman numerals to their integer values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    # Convert input to uppercase to handle lowercase numerals
    numeral = numeral.upper()
     # Handle empty string
    if not numeral:
        return 0
    
    # Check for invalid characters
    for char in numeral:
        if char not in roman_values:
            raise ValueError(f"Invalid Roman numeral character: {char}")
        total = 0
    # Iterate through the string up to the second-to-last character
    for i in range(len(numeral) - 1):
        current = roman_values[numeral[i]]
        next_val = roman_values[numeral[i + 1]]
        # If current value is less than the next, subtract it (subtractive notation)
        if current < next_val:
            total -= current
        else:
            total += current