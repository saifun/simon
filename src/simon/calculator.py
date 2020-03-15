
def add(num1, num2):
    return num1 + num2

def divide(num1, num2):
    return num1 / num2

def sub(a, b):
    return a - b

def mul(ar, pa):
    return ar * pa


def pow(base, exp):
    yay = 1
    for i in range(exp):
        yay = yay * base
    return yay

def power(base, exp):
    return base ** exp

def is_power_of_two(num):
    if num == 1:
        return True
    while num != 2:
        num = num / 2
        if num < 1:
            return False
    return True

def fac(num):
    result = 1
    for i in range(1, num + 1):
        result = result * i
    return result

def recursion_factorial(number):
    if number == 1 or number == 0:
        return 1
    return number * recursion_factorial(number - 1)


def main():
    print('Pasi', "Arbel")
    print(recursion_factorial(5))
    print(recursion_factorial(7))
    print(recursion_factorial(1))
    print(recursion_factorial(2))
    print(recursion_factorial(0))
    print(recursion_factorial(100))
    print(recursion_factorial(1000))
    print(recursion_factorial(10000))
    # print(add(7, 5))
    # print(pow(100, 3))
    # print(power(11, 2))
    # print(is_power_of_two(32))
    # print(is_power_of_two(17))
    # print(is_power_of_two(1))
    # print(is_power_of_two(2))
    # print(is_power_of_two(0))
    # print(is_power_of_two(7.3))
    # print(is_power_of_two(1.4))

if __name__ == '__main__':
    main()