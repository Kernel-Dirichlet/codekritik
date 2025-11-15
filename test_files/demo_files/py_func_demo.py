from typing import Callable

def third_order_function(f: Callable[[Callable[[int], int]], int]) -> Callable[[int], int]:
    def wrapper(x: int) -> int:
        return f(lambda y: y * 2)(x)
    return wrapper

def second_order_function(f: Callable[[int], int]) -> int:
    return f(5)

def simple_function(x: int) -> int:
    return x + 1

@third_order_function
def decorated_function(f: Callable[[int], int]) -> int:
    return f(10)

def utility_function(x: int) -> int:
    return simple_function(x) * 2

def main():
    result = second_order_function(utility_function)
    print(f"Result: {result}")
    
    decorated_result = decorated_function(3)
    print(f"Decorated result: {decorated_result}")

if __name__ == "__main__":
    main()
