import math


def printFizzBuzzResult(num):
    if not isinstance(num, (int, float)):
        print("数字を入力してください")
        return

    if math.floor(num) != num:
        print("整数を入力してください")
        return

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print("FizzでもBuzzでもない")


printFizzBuzzResult(3)
printFizzBuzzResult(5)
printFizzBuzzResult(15)
printFizzBuzzResult(1)
printFizzBuzzResult(0.1)
printFizzBuzzResult("number")
