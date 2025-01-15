#date: 15 jan 2025


def primes(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a=int(input("enter how man prime no. you want:-  "))
nprime=[]
num=2
while len(nprime)<a:
    if primes(num):
        nprime.append(num)
    num+=1
print(nprime)