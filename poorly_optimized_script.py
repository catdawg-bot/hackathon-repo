# Optimized version of the script
# with performance improvements and better practices
import time
import random
import string
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    """Recursive fibonacci with memoization - linear time complexity"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def efficient_string_operations():
    """Efficient string concatenation and operations"""
    # Using join instead of concatenation in a loop
    result = ",".join(str(i) for i in range(1000))
    
    # Using join instead of concatenation in a loop
    words = ["hello", "world", "this", "is", "fast"]
    final_string = " ".join(words)
    
    return result, final_string


def good_list_operations():
    """Efficient list operations"""
    # Creating lists efficiently
    numbers = list(range(10000))
    
    # Using set to find duplicates
    duplicates = list(set([num for num in numbers if numbers.count(num) > 1]))
    
    # Efficient filtering using list comprehension
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    # Sorting the list once
    numbers.sort()
    
    return even_numbers, duplicates


def efficient_file_operations():
    """Efficient file I/O operations"""
    filename = "temp_test_file.txt"
    
    # Writing file efficiently
    with open(filename, 'w') as f:
        text = "This is a test file with some content to write quickly."
        f.write(text)
    
    # Reading file efficiently
    with open(filename, 'r') as f:
        content = f.read()
    
    # Combining file operations
    with open(filename, 'r') as f:
        lines = f.readlines()
        word_count = len(content.split())
        char_count = len(content)
    
    # Clean up
    import os
    os.remove(filename)
    
    return content, len(lines), word_count, char_count


def avoid_redundant_calculations():
    """Avoiding redundant calculations"""
    results = []
    
    # Calculating expensive operation once
    expensive_calc = sum(x**2 for x in range(1000))
    for i in range(100):
        results.append(expensive_calc + i)
        
        # Calculating pi approximation once
        pi_approx = 4 * sum((-1)**j / (2*j + 1) for j in range(1000))
        results.append(pi_approx)
    
    return results
