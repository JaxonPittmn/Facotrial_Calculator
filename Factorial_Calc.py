def factorial(num):
    #base case
    if num == 1:
        return num
    #recursive case
    return num * factorial(num - 1)
print(factorial(4))
