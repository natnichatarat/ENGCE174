def halfPyramid(num):
    result = ""
    for i in range(num):
        for j in range(i + 1):
            result += '*'
        result += '\n'
    return result

def invertedHalfPyramid(num):
    result = ""
    for i in range(num):
        for j in range(i, num):
            result += '*'
        result += '\n'
    return result

def fullPyramid(num):
    result = ""
    for i in range(num):
        for x in range(num - i - 1):
            result += ' '
        for j in range(i + 1):
            result += '* '
        result += '\n'
    return result

def invertedFullPyramid(num):
    result = ""
    for i in range(num):
        for x in range(i):
            result += ' '
        for j in range(num - i):
            result += '* '
        result += '\n'
    return result

def triangleStar(num):
    result = ""
    space = 2 * num - 2
    for i in range(num):
        for j in range(space):
            result += " "
        space = space - 2
        for j in range(i + 1):
            result += "* "
        result += '\n'
    return result

def generatePyramids():
    return halfPyramid, invertedHalfPyramid, fullPyramid, invertedFullPyramid, triangleStar

num = int(input("Enter a number: "))

print('Half Pyramid:')
print(halfPyramid(num))
print('-----------------------')
print('Inverted Half Pyramid:')
print(invertedHalfPyramid(num))
print('-----------------------')
print('Full Pyramid:')
print(fullPyramid(num))
print('-----------------------')
print('Inverted Full Pyramid:')
print(invertedFullPyramid(num))
print('-----------------------')
print('Triangle Star:')
print(triangleStar(num))
