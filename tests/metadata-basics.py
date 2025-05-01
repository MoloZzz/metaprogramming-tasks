def foo(x: int) -> int:
    """Функція повертає квадрат числа."""
    return x*x

print(foo.__doc__)            # Метадані: опис функції
print(foo.__annotations__)    # Метадані: {'x': <class 'int'>, 'return': <class 'int'>}