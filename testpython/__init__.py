"""
testpython - یک پروژه آماده پایتون
A ready-made Python project with sample functionality.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .calculator import Calculator
from .utils import greet, format_date

__all__ = ["Calculator", "greet", "format_date"]
