import time

def timer(func):
    # Define a decorator function to measure the execution time of a function
    def wrapper(*args, **kwargs):
        start = time.time()
        # Call the original function
        result = func(*args, **kwargs)
        end = time.time()
        # Calculate the execution time
        print(f"Elapsed time: {end - start:.6f}s")
        return result
    return wrapper