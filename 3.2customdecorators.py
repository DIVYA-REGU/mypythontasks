import time

# Step 1: Timing Decorator
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of '{func.__name__}': {execution_time:.4f} seconds")
        return result
    return wrapper

# Step 2: Logger Decorator
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling '{func.__name__}' with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned: {result}")
        return result
    return wrapper

# Step 3: Apply multiple decorators
@timing_decorator
@logger_decorator
def sample_function(x, y):
    """Sample function that adds two numbers."""
    time.sleep(1)  # Simulate a time-consuming operation
    return x + y

# Testing the combined decorators
print("Testing combined decorators:")
sample_function(5, 10)

# Step 4: Parameterized Decorator
def repeat(n):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator_repeat

# Using the parameterized decorator
@repeat(3)
def greet(name):
    """Function to greet a person."""
    return f"Hello, {name}!"

# Testing the parameterized decorator
print("\nTesting parameterized decorator:")
greetings = greet("Aadhira")
print(greetings)
