
import time
import random
import string

def slow_fibonacci(n):
    """Recursive fibonacci without memoization - exponential time complexity"""
    if n <= 1:
        return n
    return slow_fibonacci(n-1) + slow_fibonacci(n-2)

def inefficient_string_operations():
    """Terrible string concatenation and operations"""
    result = ""
    # Using string concatenation in a loop instead of join
    for i in range(1000):
        result = result + str(i) + ","
    
    # Unnecessary string operations
    words = ["hello", "world", "this", "is", "slow"]
    final_string = ""
    for word in words:
        for char in word:
            final_string += char
        final_string += " "
    
    return result, final_string

def bad_list_operations():
    """Inefficient list operations and nested loops"""
    # Creating lists inefficiently
    numbers = []
    for i in range(10000):
        numbers.append(i)
    
    # Nested loops when not necessary
    duplicates = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                duplicates.append(numbers[i])
    
    # Inefficient filtering
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    
    # Sorting the same list multiple times
    for _ in range(5):
        numbers.sort()
    
    return even_numbers, duplicates

def wasteful_file_operations():
    """Inefficient file I/O operations"""
    filename = "temp_test_file.txt"
    
    # Writing file one character at a time
    with open(filename, 'w') as f:
        text = "This is a test file with some content to write slowly."
        for char in text:
            f.write(char)
            f.flush()  # Unnecessary flush on every character
    
    # Reading file one character at a time
    content = ""
    with open(filename, 'r') as f:
        while True:
            char = f.read(1)
            if not char:
                break
            content += char
    
    # Multiple file operations that could be combined
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    with open(filename, 'r') as f:
        word_count = len(f.read().split())
    
    with open(filename, 'r') as f:
        char_count = len(f.read())
    
    # Clean up
    import os
    os.remove(filename)
    
    return content, len(lines), word_count, char_count

def redundant_calculations():
    """Performing the same calculations multiple times"""
    results = []
    
    for i in range(100):
        # Calculating the same expensive operation multiple times
        expensive_calc = sum([x**2 for x in range(1000)])  # Should be cached
        results.append(expensive_calc + i)
        
        # More redundant math
        pi_approx = 0
        for j in range(1000):
            pi_approx += ((-1)**j) / (2*j + 1)
        pi_approx *= 4
        results.append(pi_approx)
    
    return results
