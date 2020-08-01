def fibonacci_generator(n):
    a, b = 0, 1
    for i in range(0, n):
        yield a
        a, b = a + b, a


def fibonacci_iterative(n):
    a, b = 0, 1
    result = list()
    for i in range(0, n):
        result.append(a)
        a, b = a + b, a
    return result


def fibonacci_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


if __name__ == '__main__':
    number = 9

    fibonacci_list = list()
    for n in fibonacci_generator(number):
        fibonacci_list.append(n)
    print(fibonacci_list)

    print(fibonacci_iterative(number))

    print(fibonacci_recursive(number))

