import time

# Logging Decorator
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Logging: {func.__name__} was called.")
        return func(*args, **kwargs)
    return wrapper

# Timing Decorator
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution Time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@log_decorator
@time_decorator
def sample_function(x, y):
    time.sleep(1)
    return x + y

print(sample_function(5, 10))
