names = ["Alice","Bob","Charlie"] #list
ages = [25,30,35]
city = ["New York","Los Angeles","Chicago"]

for names,ages,city in zip(names,ages,city):
    print(f"{names} is {ages} years old and lives in {city}")