set1 = {1,2,3,4}
set2 = {3,4,5,6}

set1.add(5)

set2.discard(6) #remove

print('Is set1 a subset of set2?',set1.issubset(set2))
print('Is set1 a subset of set1?',set2.issubset(set1))