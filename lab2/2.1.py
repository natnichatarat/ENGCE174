def halfPyramid():
    num = int(input("Enter a number: ")) 
    for i in range(num):
        for j in range(i + 1):
            print('*', end='')
        print()
def invertedHalfPyramid():
    num = int(input("Enter a number: ")) 
    for i in range(num):
        for j in range(i,5):
            print('*',end='')
        print()
def fullPyramid():
    num = int(input("Enter a number: ")) 
    for i in range(num):
        for x in range(num - i - 1):
            print(' ', end='')
        for j in range(i + 1):
            print('* ', end='')
        print()

def invertedFullPyramid():
    num = int(input("Enter a number: ")) 
    for i in range(num):
        for x in range(i):
            print(' ', end='')
        for j in range(num - i):
            print('* ', end='')
        print()

def TriangleStar():
    num = int(input("Enter a number: ")) 
    space = 2 * num - 2
    for i in range(num):
        for j in range(space):
            print(" ", end="")
        space = space - 2
        for j in range(i + 1):
            print("* ", end="")
        print()
halfPyramid()
print('-----------------------')
invertedHalfPyramid()
print('-----------------------')
fullPyramid()
print('-----------------------')
invertedFullPyramid()
print('-----------------------')
TriangleStar()