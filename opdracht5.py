import math

numbers = list(range(1, 31))
for number in numbers:
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    if result == "":
        result = number
    print(result)            

# Breaks en Continues
numbers = list(range(1,100))
for number in numbers:
    is_prime = True
    for deler in numbers:
        if deler < number and deler > 1:
            if number % deler == 0:
                is_prime = False
                break
    if is_prime:
        print(number)        