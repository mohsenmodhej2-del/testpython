"""
Main application - برنامه اصلی
Entry point for the testpython application.
"""

from testpython import Calculator, greet, format_date
from testpython.utils import is_even, is_prime, fibonacci


def main():
    """Main function to demonstrate the application."""
    print("=" * 50)
    print("Welcome to testpython - خوش آمدید به testpython")
    print("=" * 50)
    print()
    
    # Greeting example
    print("1. Greeting Example:")
    print(greet("Mohammad"))
    print(greet(""))
    print()
    
    # Date formatting example
    print("2. Date Formatting Example:")
    print(f"Current date and time: {format_date()}")
    print()
    
    # Calculator example
    print("3. Calculator Example:")
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 * 5 = {calc.multiply(10, 5)}")
    print(f"10 / 5 = {calc.divide(10, 5)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")
    print()
    
    # Number checking example
    print("4. Number Checking Example:")
    test_numbers = [2, 7, 10, 15, 17]
    for num in test_numbers:
        even_status = "even (زوج)" if is_even(num) else "odd (فرد)"
        prime_status = "prime (اول)" if is_prime(num) else "not prime (غیر اول)"
        print(f"{num} is {even_status} and {prime_status}")
    print()
    
    # Fibonacci example
    print("5. Fibonacci Sequence Example:")
    fib_seq = fibonacci(10)
    print(f"First 10 Fibonacci numbers: {fib_seq}")
    print()
    
    print("=" * 50)
    print("Demo completed successfully! - نمایش با موفقیت تکمیل شد!")
    print("=" * 50)


if __name__ == "__main__":
    main()
