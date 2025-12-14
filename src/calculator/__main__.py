"""Main entry point for running the calculator as a module."""

from calculator import Calculator


def main():
    """Run the calculator in interactive mode."""
    print("=== Calculator ===")
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("0. Exit")
    print()

    calc = Calculator()

    while True:
        try:
            choice = input("Choose an operation (0-6): ").strip()

            if choice == "0":
                print("Goodbye!")
                break

            if choice == "6":
                num = float(input("Enter a number: "))
                result = calc.square_root(num)
                print(f"√{num} = {result}\n")
            elif choice in ["1", "2", "3", "4", "5"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = calc.add(num1, num2)
                    print(f"{num1} + {num2} = {result}\n")
                elif choice == "2":
                    result = calc.subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}\n")
                elif choice == "3":
                    result = calc.multiply(num1, num2)
                    print(f"{num1} × {num2} = {result}\n")
                elif choice == "4":
                    result = calc.divide(num1, num2)
                    print(f"{num1} ÷ {num2} = {result}\n")
                elif choice == "5":
                    result = calc.power(num1, num2)
                    print(f"{num1} ^ {num2} = {result}\n")
            else:
                print("Invalid choice. Please try again.\n")

        except ValueError as e:
            print(f"Error: {e}\n")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
