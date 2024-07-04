cities = {
    'New York': [32,25,30,28,35],
    'Los Angeles': [75,68,72,70,80],
    'Chicago' : [20,18,22,25,15]
}
#dictionary of lists
averages = {city: sum(temps) / len(temps) for city,temps in cities.items()}
print("Averages temperatures:",averages)