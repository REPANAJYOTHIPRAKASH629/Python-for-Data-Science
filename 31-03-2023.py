
#1

a = int(input("Enter a value : "))
for i in range(1,a+1):
    print(i)
print()

#2
    
a = eval(input("Enter a value : "))
b = []
c = []
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
print("Even Numbers are : ",b)
print("Odd Numbers are ",c)
print()


#3

n = int(input("Enter a number to check ood/even : "))
if n%2==0:
    print("Given {} is even".format(n))
else:
    print("Given {} is odd".format(n)                                                                                                                                                                   )
print()


#4
    
s = input("Enter your string : ")
a = ''
b = ''
for i in s:
    if i in 'aeiouAEIOU':
        a+=i
    else:
        b+=i
print("Voewls are : ",a)
print("Consonants are : ",b)
print()

#5

a = eval(input("Enter list 1 : "))
b = eval(input("Enter list 2 : "))
a.extend(b)
print(a)
print()


#6

a = eval(input("Enter list of elements : "))
b = 0
c = 0
for i in a:
    if i%2==0:
        b+=i
    else:
        c+=i
print("Even Numbers are : ",b)
print("Odd Numbers are ",c)
print()


#7

a = eval(input("Enter list of elements : "))
b = 0
c = 0
for i in a:
    if i%2==0:
        b+=i*i
    else:
        c+=i*i
print("Even Numbers are : ",b)
print("Odd Numbers are ",c)
print()


# 8 simple calculator

a = float(input("enter first number : "))
b = float(input("enter second number : "))
print('''\t1.Addition
        2.Substraction
        3.Multiplication
        4.Division
        5.Modulus
        6.Exit''')
op = int(input("enter your option : "))
if op == 1:
    print(a+b)
elif op == 2:
    print(a-b)
elif op == 3:
    print(a*b)
elif op == 4:
    print(a/b)
elif op == 5:
    print(a%b)
elif op == 6:
    print("Exit")
print()


# 9 linear search

a = eval(input("Enter some elements : "))
b = int(input("Enter which element you want to search : "))
if len(a)<=0:
    print("List is empty!.")
else:
    for i in range(len(a)):
        if a[i] == b :
            print("Element is found at position",i+1)
            break
    else:
        print("Element is not found")
print()


# 10 Second largest value in list

l = eval(input("Enter the list : "))
maxx = l[0]
second = 0
for i in l:
    if i>maxx:
        second = maxx
        maxx = i
print("Second largest value is ",second)
print()


