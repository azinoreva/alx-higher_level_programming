#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        num1 = int(a)
        num2 = int(b)
        result = num1 / num2
    except ValueError:
        print("Error: Input must be integers.")
        return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    finally:
        print("Inside result: {:}".format(result), end=" ")
        return result
