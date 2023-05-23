
# 1. Print 1 to n numbers

def natural(n):
    for i in range(1,n+1):
        print(i,end=" ")



# 2. check even or odd number

def evenorodd(n):
    if n%2==0:
        return "given number is even"
    else:
        return "given number is odd"



# 3. print seperately even and odd numbers

def eo(n):
    a = []
    b = []
    for i in n:
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    print(a)
    print(b)





# 4. find the voewls and consonents seperately

def vowels(s):
    a = ''
    b = ''
    for i in s:
        if i in 'AEIOUaeiou':
            a+=i
        else:
            b+=i
    return a,b





# 5 sum of all even and odd numbers seperately

def eo(n):
    a,b = 0,0
    for i in n:
        if i%2==0:
            a+=i
        else:
            b+=i
    print(a)
    print(b)




# 6  sum of all even and odd numbers squares

def eo(n):
    a,b = 0,0
    for i in n:
        if i%2==0:
            a+=i*i
        else:
            b+=i*i
    print(a)
    print(b)




# 7 simple calculator using functions




def calculator(op):
    if op==1:
        print(a+b)
    elif op==2:
        print(a-b)
    elif op==3:
        print(a*b)
    elif op==4:
        print(a/b)
    elif op==5:
        print(a%b)
    else:
        print(exit)
    return





# 1 wapp using function print the number even and odd between 200 and 250

def evenodd(ll,ul):
    a=[]
    b=[]
    for i in range(ll,ul+1):
        if i%2==0:
            a.append(i)
        else:
            b.append(i)
    return a,b



# 2 wapp using function between 700 and 900 which are divisible by 13 and 17

def divisble(ll,ul):
    for i in range(ll,ul+1):
        if i%13==0 and i%17==0:
            print(i)
        else:
            pass



# 3 find the sum of sequence 1+22+3+4....n

def sequence(n):
    a = 0
    for i in range(1,n+1):
        if i%2==0:
            a+=i**2
        else:
            a+=i                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    return a



# 4 find the sequence 13-23+33-43...n 

def alterseq(n):
    a = 0
    b = 0
    for i in range(1,n):
        if i%2==0:
            a+=i**3
        else:
            b+=i**3
    return b-a

