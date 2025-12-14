"""Calculator module with basic mathematical operations."""


class Calculator:
    """A simple calculator class for basic mathematical operations."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b
        """
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b
        """
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b
        """
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide two numbers.

        Args:
            a: First number (numerator)
            b: Second number (denominator)

        Returns:
            Quotient of a and b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        """Raise a number to a power.

        Args:
            a: Base number
            b: Exponent

        Returns:
            a raised to the power of b
        """
        return a ** b

    @staticmethod
    def square_root(a: float) -> float:
        """Calculate the square root of a number.

        Args:
            a: Number to calculate square root of

        Returns:
            Square root of a

        Raises:
            ValueError: If a is negative
        """
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return a ** 0.5
