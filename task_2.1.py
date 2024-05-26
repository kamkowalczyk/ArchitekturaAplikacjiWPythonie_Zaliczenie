import functools
import inspect

def log_parameters(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_signature = inspect.signature(func)
        parameters = func_signature.parameters
        param_types = {name: param.annotation for name, param in parameters.items()}
        log_message = {name: str(param_type) for name, param_type in param_types.items()}
        print(f"Parameters of function '{func.__name__}': {log_message}")
        return func(*args, **kwargs)
    return wrapper

@log_parameters
def example_function(a: int, b: str, c: float):
    print(a, b, c)

example_function(1, 'test', 3.14)
