def square(func):
    def wrapper(a,b):
        return func(a,b) * func(a,b)
    return wrapper


@square
def add(a,b):
    return a+b
print(add(5,3))            