"""
Given a binary number as a string, convert it to a decimal number.
"""
def binary_to_decimal(binary_str):
    decimal_value = 0
    power = 0
    
    # Reverse the binary string to process from least significant bit
    binary_str = binary_str[::-1]
    
    for digit in binary_str:
        if digit == '1':
            decimal_value += 2 ** power
        power += 1
        
    return decimal_value
# Example usage:
binary_str = "1011"
decimal_number = binary_to_decimal(binary_str)
print(decimal_number)  # Output: 11
