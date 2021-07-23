#Bai 1
rdnum = int(input("1.Nhap mot so bat ky: "))
while rdnum>0:
    a = int(rdnum%10)
    print(a)
    rdnum//=10

#Bai 2
ib = float(input("2. Nhap so du ban dau: "))
ap = float(input("Nhap phan tram lai: "))
db = float(input("Nhap so du mong muon: "))
while ib<db:
    ib=float((ib/100)*(100+ap))
    print(ib)