# Write a generator function that generates Fibonacci numbers up to a specified limit.

def fibo_generator(steps):
    a = 0
    b = 1
    for _ in range(steps):
        yield b
        a, b = b, a + b

iterations = 50

obj = fibo_generator(iterations)
for _ in range(iterations):
    print(next(obj))
