numbers = [1,2,3,4,5]

print("First element :",numbers[0]) #out 1
print("First element :",numbers[-1]) #out 5

print("Sliced element :",numbers[2:4]) #out [3,4]

numbers.append(6)
print("After append:",numbers) #out [1,2,3,4,5,6]

numbers.remove(3)
print("After removal:",numbers) #out [1,2,4,5,6]