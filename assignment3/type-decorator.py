def type_converter(type_of_output):
    # 1) This outer function receives the type you want (str, int, float...)
    def decorator(func):
        # 2) This function receives the function you're decorating
        def wrapper(*args, **kwargs):
            # 3) This runs when the decorated function is called
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return decorator


@type_converter(str)
def return_int():
    return 5


@type_converter(int)
def return_string():
    return "not a number"


# --- mainline code the assignment asked for ---
y = return_int()
print(type(y).__name__)  # This should print "str"

try:
    y = return_string()
    print("shouldn't get here!")
except ValueError:
    print("can't convert that string to an integer!")
