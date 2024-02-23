import time


def delay_devorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@delay_devorator
def say_hello():
    print("Hello")

@delay_devorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")


say_hello()
say_greeting()
say_bye()
