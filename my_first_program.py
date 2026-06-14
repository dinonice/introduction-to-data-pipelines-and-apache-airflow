print("Hello World!")
print("Data Pipeline")

name = "Nanapas Nice"
number = 10
a = 5
b = 9

#python ทำงานจากบนลงล่าง ซึ่งจะเก็บตัวแปรใหม่เสมอ

print(name)
#คำนวน
c = a  + b
c = c * 10 #คูณ
print(c)

print(5 % 4) #หาร
print(5 % 2)

#if: eles: คือการสร้างเงื่อนไขคือ if ถ้า ...... แต่ถ้าไม่ใช้จะเข้าเงื่อนไข eles 
if c > 150:
    c = 100
    a = 100
    b = 100
else: 
    c = 9
    a = 9
    b = 9

print(a, b, c)

#กรณีที่ต้องการทำซ้ำ lope [] = การสร้าง element ที่ข้างในมีค่าตามกำหนด

l = [1, 2, 3, 4, 5]
for item in l:  
    if item % 2 == 0:
        print(item)
        

