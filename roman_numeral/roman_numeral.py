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