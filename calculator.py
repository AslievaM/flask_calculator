import math

class Calculator:
    """Handles all mathematical operations."""

    SUPPORTED_OPERATIONS = ['+', '-', '*', '/', 'sqrt', 'pow', 'sin', 'cos', 'tan', 'log', 'log10']

    def calculate(self, operation, num1, num2=None):

        if operation not in self.SUPPORTED_OPERATIONS:
            raise ValueError("Unsupported operation")

        # Two-number operations
        if operation in ['+', '-', '*', '/', 'pow']:
            if num2 is None:
                raise ValueError("num2 is required for this operation")

            if operation == '+':
                return num1 + num2
            elif operation == '-':
                return num1 - num2
            elif operation == '*':
                return num1 * num2
            elif operation == '/':
                if num2 == 0:
                    raise ZeroDivisionError()
                return num1 / num2
            elif operation == 'pow':
                return math.pow(num1, num2)

        # One-number operations
        else:
            if operation == 'sqrt':
                if num1 < 0:
                    raise ValueError("Square root of a negative number is not defined")
                return math.sqrt(num1)

            elif operation in ['sin', 'cos', 'tan']:
                radians = math.radians(num1)
                if operation == 'sin':
                    return math.sin(radians)
                elif operation == 'cos':
                    return math.cos(radians)
                elif operation == 'tan':
                    return math.tan(radians)

            elif operation == 'log':
                if num1 <= 0:
                    raise ValueError("Logarithm requires a positive number")
                return math.log(num1)

            elif operation == 'log10':
                if num1 <= 0:
                    raise ValueError("Logarithm requires a positive number")
                return math.log10(num1)

    def format_expression(self, operation, num1, num2=None):

        if operation in ['+', '-', '*', '/']:
            return f"{num1} {operation} {num2}"

        elif operation == 'pow':
            return f"{num1} ^ {num2}"

        else:
            return f"{operation}({num1})"