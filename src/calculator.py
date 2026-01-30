def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")

    return x + y


def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y


def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
        Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y


def fun4(x, y, z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    """
    total_sum = x + y + z
    return total_sum


def fun5(x, y):
    """
    Divides two numbers with zero-division handling.
    Args:
        x (int/float): Dividend.
        y (int/float): Divisor.
    Returns:
        float: Quotient of x divided by y.
    Raises:
        ValueError: If x or y is not a number.
        ZeroDivisionError: If y is zero.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y

def fun6(x):
    """
    Squares a number.
    Args:
        x (int/float): Input number.
    Returns:
        int/float: Square of x.
    Raises:
        ValueError: If x is not a number.
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a number.")
    return x ** 2


def fun7(n):
    """
    Calculates factorial of a non-negative integer.
    Args:
        n (int): Non-negative integer.
    Returns:
        int: Factorial of n.
    Raises:
        ValueError: If n is not a non-negative integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fun8(n):
    """
    Calculates the factorial of a non-negative integer.
    Args:
        n (int): Non-negative integer.
    Returns:
        int: Factorial of n.
    Raises:
        ValueError: If n is not an integer or is negative.
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fun9(x, y):
    """
    Calculates x raised to the power y.
    Args:
        x (int/float): Base.
        y (int): Exponent.
    Returns:
        int/float: x to the power y.
    Raises:
        ValueError: If inputs are not valid numbers or exponent is not an integer.
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Base must be a number.")
    if not isinstance(y, int):
        raise ValueError("Exponent must be an integer.")

    return x ** y

def fun10(x, y):
    """
    Calculates x raised to the power y.
    Args:
        x (int/float): Base.
        y (int): Exponent.
    Returns:
        int/float: x to the power y.
    Raises:
        ValueError: If inputs are not valid numbers or exponent is not an integer.
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Base must be a number.")
    if not isinstance(y, int):
        raise ValueError("Exponent must be an integer.")

    return x ** y

# f1_op = fun1(2,3)
# f2_op = fun2(2,3)
# f3_op = fun3(2,3)
# f4_op = fun4(f1_op,f2_op,f3_op)