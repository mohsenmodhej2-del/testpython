# testpython API Documentation

## Modules

### testpython.calculator

Calculator module providing basic arithmetic operations.

#### Class: Calculator

A simple calculator class for basic arithmetic operations.

**Methods:**

- `__init__()`: Initialize the calculator
- `add(a, b)`: Add two numbers
- `subtract(a, b)`: Subtract b from a
- `multiply(a, b)`: Multiply two numbers
- `divide(a, b)`: Divide a by b (raises ValueError if b is zero)
- `power(base, exponent)`: Calculate base raised to the power of exponent
- `get_result()`: Get the last calculated result

**Example:**

```python
from testpython import Calculator

calc = Calculator()
result = calc.add(10, 5)
print(result)  # Output: 15
```

### testpython.utils

Utility functions for common tasks.

#### Functions:

**greet(name)**
- Generate a greeting message
- Args: name (str) - Name of the person to greet
- Returns: str - Greeting message

**format_date(date=None, format_string="%Y-%m-%d %H:%M:%S")**
- Format a date object to a string
- Args:
  - date (datetime, optional): Date to format. Defaults to current datetime
  - format_string (str, optional): Format string
- Returns: str - Formatted date string

**is_even(number)**
- Check if a number is even
- Args: number (int) - Number to check
- Returns: bool - True if even, False otherwise

**is_prime(number)**
- Check if a number is prime
- Args: number (int) - Number to check
- Returns: bool - True if prime, False otherwise

**fibonacci(n)**
- Generate Fibonacci sequence up to n terms
- Args: n (int) - Number of terms
- Returns: list - List of Fibonacci numbers

**Example:**

```python
from testpython.utils import is_prime, fibonacci

print(is_prime(17))  # Output: True
print(fibonacci(5))  # Output: [0, 1, 1, 2, 3]
```

## Main Application

The main application (`testpython.main`) provides a demonstration of all features.

**Running the application:**

```bash
python -m testpython.main
# or
testpython
```
