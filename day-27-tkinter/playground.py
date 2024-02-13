def add(*args):
    print(type(args))
    print(args)

    sum = 0
    for v in args:
        sum += v
    return sum


print(add(1,2,3,4,5,6))


def calculate(n, **kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f"{key}: {value}")

    print(kwargs["add"])

    return (n + kwargs["add"]) * kwargs["multiply"]


print(calculate(2, add=3, multiply=2))


class Car:
    def __init__(self, **kw):
        self.model = kw.get("model")


car1 = Car(model = "GT-R")
car2 = Car()