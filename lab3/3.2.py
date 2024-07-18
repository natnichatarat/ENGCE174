def halfpyramid(n):
    n = int(n)  
    if n > 0:
        halfpyramid(n - 1)
        print('* ' * n)

def invertedHalfPyramid(n):
    n = int(n)  
    if n > 0:
        print('* ' * n)
        invertedHalfPyramid(n - 1)

def fullPyramid(n, current=1):
    n = int(n)  
    if current > n:
        return
    spaces = ' ' * (n - current)
    stars = '* ' * current
    print(spaces + stars)
    fullPyramid(n, current + 1)

def invertedFullPyramid(n, current=1):
    n = int(n)  
    if current > n:
        return
    spaces = ' ' * (current - 1)
    stars = '* ' * (n - current + 1)
    print(spaces + stars)
    invertedFullPyramid(n, current + 1)

def inver(n, current=1):
    n = int(n) 
    if current > n:
        return
    spaces = ' ' * (n - current)
    stars = '*' * (current)
    print(spaces + stars)
    inver(n, current + 1)


n = input("Enter a number: ")


print("Half Pyramid:")
halfpyramid(n)
print('-----------------------')

print("Inverted Half Pyramid:")
invertedHalfPyramid(n)
print('-----------------------')

print("Full Pyramid:")
fullPyramid(n)
print('-----------------------')

print("Inverted Full Pyramid:")
invertedFullPyramid(n)
print('-----------------------')

print("Inverted Pyramid:")
inver(n)
