from functools import wraps
import types

def log_methods(cls):
    for name in dir(cls):
        # Пропускаємо спеціальні методи та атрибути
        if name.startswith('__'):
            continue
        attr = getattr(cls, name)
        # Перевіряємо, чи є атрибут функцією або методом
        if callable(attr) and (isinstance(attr, (types.FunctionType, types.MethodType))):
            @wraps(attr)
            def wrapper(self, *args, **kwargs):
                print(f"Виклик методу {cls.__name__}.{name} з аргументами {args}, {kwargs}")
                result = attr(self, *args, **kwargs)
                print(f"Метод {cls.__name__}.{name} повернув {result}")
                return result
            setattr(cls, name, wrapper)
    return cls

@log_methods
class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b

# Тестування
calc = Calculator()
calc.add(3, 5)
calc.multiply(4, 6)