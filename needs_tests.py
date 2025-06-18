import math
import re
from typing import List, Dict, Optional, Union, Tuple
from datetime import datetime, timedelta
import json

def calculate_bmi(weight: float, height: float) -> float:
    """Calculate Body Mass Index from weight (kg) and height (m)."""
    if height <= 0:
        raise ValueError("Height must be positive")
    if weight <= 0:
        raise ValueError("Weight must be positive")
    return weight / (height ** 2)

def is_valid_email(email: str) -> bool:
    """Check if an email address is valid using regex."""
    if not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def fibonacci_sequence(n: int) -> List[int]:
    """Generate fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

def find_prime_factors(n: int) -> List[int]:
    """Find all prime factors of a given number."""
    if n <= 1:
        return []
    
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def merge_dictionaries(*dicts: Dict) -> Dict:
    """Merge multiple dictionaries, with later values overriding earlier ones."""
    if not dicts:
        return {}
    
    result = {}
    for d in dicts:
        if not isinstance(d, dict):
            raise TypeError(f"Expected dict, got {type(d)}")
        result.update(d)
    return result

def calculate_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    """Calculate Euclidean distance between two 2D points."""
    if len(point1) != 2 or len(point2) != 2:
        raise ValueError("Points must be 2D tuples")
    
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def parse_json_safe(json_string: str) -> Optional[Union[Dict, List]]:
    """Safely parse JSON string, returning None if invalid."""
    try:
        return json.loads(json_string)
    except (json.JSONDecodeError, TypeError):
        return None

def filter_and_sort_numbers(numbers: List[Union[int, float]], 
                          min_value: Optional[float] = None,
                          max_value: Optional[float] = None,
                          reverse: bool = False) -> List[Union[int, float]]:
    """Filter numbers by range and sort them."""
    if not isinstance(numbers, list):
        raise TypeError("Numbers must be a list")
    
    # Filter out non-numeric values
    numeric_values = [x for x in numbers if isinstance(x, (int, float)) and not math.isnan(x)]
    
    # Apply range filters
    if min_value is not None:
        numeric_values = [x for x in numeric_values if x >= min_value]
    if max_value is not None:
        numeric_values = [x for x in numeric_values if x <= max_value]
    
    return sorted(numeric_values, reverse=reverse)

def count_word_frequency(text: str, case_sensitive: bool = False) -> Dict[str, int]:
    """Count frequency of words in text."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string")
    
    if not case_sensitive:
        text = text.lower()
    
    # Remove punctuation and split into words
    words = re.findall(r'\b\w+\b', text)
    
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

def validate_password(password: str) -> Tuple[bool, List[str]]:
    """Validate password strength and return issues."""
    if not isinstance(password, str):
        return False, ["Password must be a string"]
    
    issues = []
    
    if len(password) < 8:
        issues.append("Password must be at least 8 characters long")
    
    if not re.search(r'[A-Z]', password):
        issues.append("Password must contain at least one uppercase letter")
    
    if not re.search(r'[a-z]', password):
        issues.append("Password must contain at least one lowercase letter")
    
    if not re.search(r'\d', password):
        issues.append("Password must contain at least one digit")
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        issues.append("Password must contain at least one special character")
    
    return len(issues) == 0, issues

def calculate_age_from_birthdate(birthdate: str, reference_date: Optional[str] = None) -> int:
    """Calculate age from birthdate string (YYYY-MM-DD format)."""
    try:
        birth = datetime.strptime(birthdate, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Birthdate must be in YYYY-MM-DD format")
    
    if reference_date:
        try:
            ref = datetime.strptime(reference_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Reference date must be in YYYY-MM-DD format")
    else:
        ref = datetime.now()
    
    if birth > ref:
        raise ValueError("Birthdate cannot be in the future")
    
    age = ref.year - birth.year
    if ref.month < birth.month or (ref.month == birth.month and ref.day < birth.day):
        age -= 1
    
    return age

def binary_search(arr: List[int], target: int) -> int:
    """Perform binary search on sorted array. Returns index or -1 if not found."""
    if not isinstance(arr, list):
        raise TypeError("Array must be a list")
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def generate_random_string(length: int, 
                         include_uppercase: bool = True,
                         include_lowercase: bool = True,
                         include_digits: bool = True,
                         include_special: bool = False) -> str:
    """Generate a random string with specified character types."""
    if length <= 0:
        raise ValueError("Length must be positive")
    
    import random
    import string
    
    chars = ""
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_digits:
        chars += string.digits
    if include_special:
        chars += "!@#$%^&*"
    
    if not chars:
        raise ValueError("At least one character type must be included")
    
    return ''.join(random.choice(chars) for _ in range(length))

def flatten_nested_list(nested_list: List) -> List:
    """Flatten a nested list of arbitrary depth."""
    result = []
    
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_nested_list(item))
        else:
            result.append(item)
    
    return result

def calculate_compound_interest(principal: float, 
                              rate: float, 
                              time: float, 
                              compound_frequency: int = 1) -> float:
    """Calculate compound interest."""
    if principal <= 0:
        raise ValueError("Principal must be positive")
    if rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if time < 0:
        raise ValueError("Time cannot be negative")
    if compound_frequency <= 0:
        raise ValueError("Compound frequency must be positive")
    
    amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    return round(amount, 2)

class BankAccount:
    """Simple bank account class for testing object-oriented functionality."""
    
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        if not account_number:
            raise ValueError("Account number cannot be empty")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        self.account_number = account_number
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount:.2f}")
    
    def withdraw(self, amount: float) -> bool:
        """Withdraw money from the account. Returns True if successful."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            return False
        
        self.balance -= amount
        self.transaction_history.append(f"Withdrew ${amount:.2f}")
        return True
    
    def get_balance(self) -> float:
        """Get current account balance."""
        return self.balance
    
    def get_transaction_history(self) -> List[str]:
        """Get list of all transactions."""
        return self.transaction_history.copy()

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
    
    return (celsius * 9/5) + 32

def find_longest_common_substring(str1: str, str2: str) -> str:
    """Find the longest common substring between two strings."""
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both inputs must be strings")
    
    if not str1 or not str2:
        return ""
    
    longest = ""
    
    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring = str1[i:j]
            if substring in str2 and len(substring) > len(longest):
                longest = substring
    
    return longest
