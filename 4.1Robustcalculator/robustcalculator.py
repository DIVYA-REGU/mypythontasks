import math

class RobustCalculator:
    def add(self, a, b):
        self.validate_input(a, b)
        return a + b

    def subtract(self, a, b):
        self.validate_input(a, b)
        return a - b

    def multiply(self, a, b):
        self.validate_input(a, b)
        return a * b

    def divide(self, a, b):
        self.validate_input(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b

    def square_root(self, a):
        self.validate_input(a)
        if a < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        return math.sqrt(a)

    def exponentiate(self, base, exponent):
        self.validate_input(base, exponent)
        return math.pow(base, exponent)

    def logarithm(self, a, base=math.e):
        self.validate_input(a)
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        return math.log(a, base)

    def validate_input(self, *args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Invalid input type: {type(arg)}. Must be int or float.")

def get_user_input():
    calculator = RobustCalculator()
    
    while True:
        print("\nAvailable operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square Root")
        print("6. Exponentiate")
        print("7. Logarithm")
        print("8. Exit")
        
        choice = input("Choose an operation (1-8): ")

        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {calculator.add(a, b)}")
                elif choice == '2':
                    print(f"Result: {calculator.subtract(a, b)}")
                elif choice == '3':
                    print(f"Result: {calculator.multiply(a, b)}")
                elif choice == '4':
                    print(f"Result: {calculator.divide(a, b)}")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '5':
            try:
                a = float(input("Enter number: "))
                print(f"Result: {calculator.square_root(a)}")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '6':
            try:
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                print(f"Result: {calculator.exponentiate(base, exponent)}")

            except Exception as e:
                print(f"Error: {e}")

        elif choice == '7':
            try:
                a = float(input("Enter number: "))
                base = input("Enter base (default is e): ")
                if base:
                    base = float(base)
                    print(f"Result: {calculator.logarithm(a, base)}")
                else:
                    print(f"Result: {calculator.logarithm(a)}")

            except Exception as e:
                print(f"Error: {e}")

        else:
            print("Invalid choice. Please select a valid operation.")

# Run the calculator
if __name__ == "__main__":
    get_user_input()
