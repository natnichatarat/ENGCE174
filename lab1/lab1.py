#list
squares = [x**2 for x in range(10)]
#Dictionry
squares_dict = {x: x**2 for x in range(5)}
#set 
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print("squares",squares)
print("squares_dict",squares_dict)
print("even_squares",even_squares)