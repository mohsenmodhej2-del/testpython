"""
Utility functions - توابع کمکی
Provides helper functions for common tasks.
"""

from datetime import datetime


def greet(name):
    """
    Generate a greeting message.
    
    Args:
        name (str): Name of the person to greet
        
    Returns:
        str: Greeting message
    """
    if not name:
        return "Hello, Guest!"
    return f"Hello, {name}!"


def format_date(date=None, format_string="%Y-%m-%d %H:%M:%S"):
    """
    Format a date object to a string.
    
    Args:
        date (datetime, optional): Date to format. Defaults to current datetime.
        format_string (str, optional): Format string. Defaults to "%Y-%m-%d %H:%M:%S".
        
    Returns:
        str: Formatted date string
    """
    if date is None:
        date = datetime.now()
    return date.strftime(format_string)


def is_even(number):
    """
    Check if a number is even.
    
    Args:
        number (int): Number to check
        
    Returns:
        bool: True if even, False otherwise
    """
    return number % 2 == 0


def is_prime(number):
    """
    Check if a number is prime.
    
    Args:
        number (int): Number to check
        
    Returns:
        bool: True if prime, False otherwise
    """
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.
    
    Args:
        n (int): Number of terms
        
    Returns:
        list: List of Fibonacci numbers
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence
