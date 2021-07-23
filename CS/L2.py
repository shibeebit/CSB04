#Bai 1
fname = input("1.First name: ")
lname = input("Last name: ")
print(lname + " " + fname)

#Bai 2
radius = float(input("2.Radius: "))
print(radius*radius*3.14)

#Bai 3
randomnum = int(input("3.Nhap mot so: "))
print(bool(randomnum<100))

#Bai 4
rds = str(input("4.Nhap 1 string: "))
rds2=rds.replace("s", "$")
rds2=rds2.replace("e", "3")
rds2=rds2.replace("o", "0")
rds2=rds2.replace("a", "@(t33nc0d3)")
print(rds2)