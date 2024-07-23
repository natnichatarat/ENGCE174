def halfpyramid(n, current=1):
    if current > n:
        return []
    return halfpyramid(n, current + 1) + ['* ' * current]

def invertedHalfPyramid(n, current=1):
    if current > n:
        return []
    return ['* ' * (n - current + 1)] + invertedHalfPyramid(n, current + 1)

def fullPyramid(n, current=1):
    if current > n:
        return []
    spaces = ' ' * (n - current)
    stars = '* ' * current
    return fullPyramid(n, current + 1) + [spaces + stars]

def invertedFullPyramid(n, current=1):
    if current > n:
        return []
    spaces = ' ' * (current - 1)
    stars = '* ' * (n - current + 1)
    return [spaces + stars] + invertedFullPyramid(n, current + 1)

def invertedPyramid(n, current=1):
    if current > n:
        return []
    spaces = ' ' * (n - current)
    stars = '*' * current
    return invertedPyramid(n, current + 1) + [spaces + stars]

def generatePatterns(n):
    return {
        "Half Pyramid": halfpyramid(n),
        "Inverted Half Pyramid": invertedHalfPyramid(n),
        "Full Pyramid": fullPyramid(n),
        "Inverted Full Pyramid": invertedFullPyramid(n),
        "Inverted Pyramid": invertedPyramid(n)
    }

def printPatterns(patterns):
    for name, pattern in patterns.items():
        print(name)
        for line in pattern:
            print(line)
        print('-----------------------')

n = int(input("Enter a number: "))
patterns = generatePatterns(n)
printPatterns(patterns)
