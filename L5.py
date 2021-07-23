#Bai 1
num_list = [7, -11, 6, 3, 1, 3, 9]

list_max = num_list[0]
list_min = num_list[0]
list_sum = 0
list_len = 0
for num in num_list:
    if num > list_max :
        list_max = num
    if num < list_min:
        list_min = num
    list_sum += num
    list_len += 1

print("Bai 1: User list is ", num_list)
print("Max: ", list_max)
print("Min: ", list_min)
print("Sum: ", list_sum)
print("Length: ", list_len)

#Bai 2
num_list2 = [1, 3, -4, -2, 5, 7, 0]
print("Bai 2: User list is ", num_list2)
neg_num = 0
for num in num_list2:
    if num == 0:
        print(0)
        negnum = 0
        break
    elif num < 0:
        neg_num += 1
if neg_num % 2 == 0 and neg_num != 0:
    print(-1)
else:
    print(1)


#Bai 3
x = int(input("Bai 3: Input n: "))
for i in range(1, x+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)

#Bai 4
a = int(input("Bai 4. Input a random number: "))
for i in range(1, a+1, +1):
    print(" " * (a-i), "*" * i)

#Bai 5
b = int(input("Bai 5. Input a random number: "))
for i in range(1, b+1, +1):
    print(" " * (b-i),"* " * i, " " * (b-i-1))

#Bai 6
num_list4 = [10, 7, 4, 6, 8, 10, 11]
c = num_list4[1] - num_list4[0]
turn = 0
most_turn = 0
d = 0
for i in range(0, len(num_list4)-1):
    if (num_list4[i+1] - num_list4[i]) == c:
        turn += 1
        if turn > most_turn:
            most_turn = turn
            d = c
    else:
        turn = 1
        c = num_list4[i+1] - num_list4[i]

print("Bai 6: User list is ", num_list4)
print(d)

#Bai 7
num_list5 = [-7, 1, 3, 5, -7, 12, 8, 3, -15, 6, -3, -4]
largest_product = num_list5[1]*num_list5[0]
for num in num_list5:
    for num2 in num_list5:
        if (num * num2) > largest_product:
            largest_product = num * num2

print("Bai 7: User list is ", num_list4)
print(largest_product)

#Bai 8
for x in range(1, int(input("Bai 8: Enter a number: "))+1):
   print(int((10**x-1)/9)**2)

#Bai 10:

num_list10 = [3,0,2,1,9,7]
print('Bai 10: User list is:', num_list10)
a10 = int(input("Bai 10: Enter a: "))
b10 = int(input("Enter b: "))
c10 = int(input("Enter c: "))
triplets = 0

for i in range(0, len(num_list10)):
    for j in range(i+1, len(num_list10)):
        for k in range(j+1, len(num_list10)):
            if (abs(num_list10[i]-num_list10[j]) <= a10) and (abs(num_list10[j]-num_list10[k]) <= b10) and (abs(num_list10[i]-num_list10[k]) <= c10):
                triplets += 1

print(triplets)

#Bai 11
def func11(num_list3):
    product = 1
    for num in num_list3:
        el_loop = 0
        for num2 in num_list3:
            if num == num2:
                el_loop += 1
        if el_loop == 1:
            product *= num

    print("Bai 11: User list is ", num_list3)
    print(product)

func11([1,6,7,4,5,5,9,8,6,7,9])

#Bai 12
full_bottles = int(input("Bai 12: Enter number of full bottles: "))
exchange = int(input("Enter number of exchange: "))
count = full_bottles 
while full_bottles//exchange != 1:
    count += full_bottles//exchange
    full_bottles = full_bottles //exchange
count += 1
print(count)

#Bai 13
lemon_list = [5,5, 5, 10, 20]
five = 0
ten = 0
twenty = 0
for lemon in lemon_list:
    if lemon == 5:
        five += 1
    elif lemon == 10:
        ten +=1
    else:
        twenty += 1

five = five - ten
five = five - (twenty * 3)
print("Bai 13: User list is", lemon_list)
print(five>0)

#Bai 15

import math
rdnum15 = int(input("Bai 15: Enter a random number: "))
sum15 = 0

for i in range(1, rdnum15):
    if rdnum15%i == 0:
        sum15 += i

print(bool(rdnum15==sum15))

#Bai 16

rdnum16 = int(input("Bai 16: Enter a random number: "))

for i in range(1, rdnum16):
    if i*i > rdnum16:
        print(i-1)
        break

#Bai 17

num_list17 = [1,7,14,11]
print('Bai 17:', num_list17)
db_num_exist = 0
for num in num_list17:
    for num2 in num_list17:
        if num2 == num * 2:
            db_num_exist = 1
            break

print(bool(db_num_exist==1))

#Bai 18
rdstr18 = str(input("Bai 18: Enter a random str: "))
char = rdstr18[0]
lcs = 1
lc = ''
cs = 1

for i in range(1, len(rdstr18)):
    if char == rdstr18[i]:
        cs += 1
    else:
        char = rdstr18[i]
        cs = 1
    if cs > lcs:
        lcs = cs
        lc = char

print(lcs*lc)


















