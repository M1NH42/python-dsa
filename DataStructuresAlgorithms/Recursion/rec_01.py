def factorial(number):
    """ Calcualtes factorial for the number."""
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5))