"""
Calculator module - ماژول ماشین حساب
Provides basic arithmetic operations.
"""


class Calculator:
    """A simple calculator class for basic arithmetic operations."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.result = 0
    
    def add(self, a, b):
        """
        Add two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        self.result = a + b
        return self.result
    
    def subtract(self, a, b):
        """
        Subtract b from a.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Difference of a and b
        """
        self.result = a - b
        return self.result
    
    def multiply(self, a, b):
        """
        Multiply two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        """
        Divide a by b.
        
        Args:
            a (float): Numerator
            b (float): Denominator
            
        Returns:
            float: Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.result = a / b
        return self.result
    
    def power(self, base, exponent):
        """
        Calculate base raised to the power of exponent.
        
        Args:
            base (float): Base number
            exponent (float): Exponent
            
        Returns:
            float: base^exponent
        """
        self.result = base ** exponent
        return self.result
    
    def get_result(self):
        """
        Get the last calculated result.
        
        Returns:
            float: The last result
        """
        return self.result
