
def sum_num(n):
    if n == 1:
        return 1
    else:
        return n + sum_num(n - 1)

def factorial(n):
    print("n:", n)
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n == 1 or n==2:
        return 1
    else:
        print("n:", n)
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))