set1 = {1,2,3,4}
set2 = {3,4,5,6}

union_set = set1 |set2
intersection_set = set1 & set2
difference_set = set1 - set2 #สมาชิกที่อยู่ใน set1 แต่ไม่อยู่ใน set2
symmetric_diffeerence_set = set1 ^ set2 #สมาชิกที่อยู่ใน set1 หรือ set2 แต่ไม่อยู่ในทั้งสองเซ็ต
print('Union:',union_set)
print ('Intersection :',intersection_set)
print ('Difference :',difference_set)
print ('Symmetric :',symmetric_diffeerence_set)