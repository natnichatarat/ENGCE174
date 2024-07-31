grades = {'Alice': 85,'Bob': 92, 'Charlie': 88, 'David': 95}
print('Bobs grade:', grades['Bob'])

grades['eve'] = 90 #เพิ่ม entry value 90

for student,grade in grades.items():
    print(f"{student}: {grade}") #วนลูปพิมพ์ชื่อแต่ละคน

print("Frank's grade:",grades.get('Frank','Grade not found')) #ดึง Frank ไม่มีให้พิมพ์