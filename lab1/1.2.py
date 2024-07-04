def fibonacci(): #generator สร้างลำดับฟีโบนักชี
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

fib = fibonacci()
print(next(fib)) #out 0
print(next(fib)) #out 1