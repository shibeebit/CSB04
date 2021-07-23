#Bai 1
n = int(input("1. Nhap so bat ky: "))
for i in range(1, n+1, +1):
    print("*"*i)
for i in range(n-1, 0, -1):
    print("*"*i)

#Bai 2
x = int(input("2. Nhap so bat ky: "))
f1 = 0
f2 = 1
for i in range(3, x+1):
    fn = f1+ f2
    f1 = f2
    f2 = fn
print(fn)

#Bai 3
import math
y = int(input("3. Nhap so bat ky: "))
while y%2 == 0:
    print(2)
    y/=2

for i in range(3, int(math.sqrt(y))+1, 2):
    while y%i == 0:
        print (i)
        y/=i
if y>2 :
    print(y)


