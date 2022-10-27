import math


def numbers(n: int) -> None:
    if n < 0:
        return
    print(n)
    numbers(n - 1)


def fib(n: int) -> int:
    if n < 0:
        print("Zla wartosc")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def power(number: int, n: int) -> int:
    i = n
    if n == 0:
        return 1
    elif n == 1:
        return number
    else:
        return number * power(number, n - 1)


def reverse(txt: str) -> str:
    if len(txt) == 0 or len(txt) == 1:
        return txt
    elif len(txt) >= 2:
        return reverse(txt[1:]) + txt[0]


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        n *= factorial(n - 1)
        return n


def prime(x: int) -> bool:
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, math.floor(math.sqrt(x)) + 1):
        if prime(i):
            if x % i == 0:
                return False
    return True





def main():
    numbers(10)
    print('')
    print(fib(9))
    print(power(2, 3))
    print(reverse('Kacper'))
    print(factorial(5))
    print(prime(4))

if __name__ == '__main__':
    main()
