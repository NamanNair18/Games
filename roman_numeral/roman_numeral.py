def roman_to_int(numeral):
     # Dictionary mapping Roman numerals to their integer values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    # Convert input to uppercase to handle lowercase numerals
    numeral = numeral.upper()
    