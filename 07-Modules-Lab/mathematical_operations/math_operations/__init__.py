from .operations import add, subtract, multiply, divide, power

def calculate_expression(expression):
    (x, sign, y) = expression.split(' ')
    x = float(x)
    y = float(y)

    if sign == "+":
        result = add(x, y)
    elif sign == "-":
        result = subtract(x, y)
    elif sign == "*":
        result = multiply(x, y)
    elif sign == "/":
        result = divide(x, y)
    elif sign == "^":
        result = power(x, y)
    else:
        raise Exception(f"Invalid sign {sign}")
    return f'{result:.2f}'
