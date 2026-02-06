def power(base, exp):
    """Calculate base raised to the power of exponent."""
    return base ** exp

def average(numbers_list):
    """Calculate the average of a list of numbers."""
    if not numbers_list:  
        return 0
    return sum(numbers_list) / len(numbers_list)