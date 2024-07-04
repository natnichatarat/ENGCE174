even_numbers = [x for x in range(10) if x % 2 == 0]
squares = [num**2 for num in even_numbers]
print("Square of even numbers",squares)