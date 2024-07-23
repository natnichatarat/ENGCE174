def halfPyramid(num):
    pattern = []
    for i in range(num):
        line = '*' * (i + 1)
        pattern.append(line)
    return pattern

def invertedHalfPyramid(num):
    pattern = []
    for i in range(num):
        line = '*' * (num - i)
        pattern.append(line)
    return pattern

def fullPyramid(num):
    pattern = []
    for i in range(num):
        line = ' ' * (num - i - 1) + '* ' * (i + 1)
        pattern.append(line)
    return pattern

def invertedFullPyramid(num):
    pattern = []
    for i in range(num):
        line = ' ' * i + '* ' * (num - i)
        pattern.append(line)
    return pattern

def triangleStar(num):
    pattern = []
    space = 2 * num - 2
    for i in range(num):
        line = ' ' * space + '* ' * (i + 1)
        space -= 2
        pattern.append(line)
    return pattern

def generatePatterns(num):
    patterns = {
        "halfPyramid": halfPyramid(num),
        "invertedHalfPyramid": invertedHalfPyramid(num),
        "fullPyramid": fullPyramid(num),
        "invertedFullPyramid": invertedFullPyramid(num),
        "triangleStar": triangleStar(num)
    }
    return patterns

def printPatterns(patterns):
    for name, pattern in patterns.items():
        print(name)
        for line in pattern:
            print(line)
        print('-----------------------')

num = int(input("Enter a number: "))
patterns = generatePatterns(num)
printPatterns(patterns)
