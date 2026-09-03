n = int(input("enter a number:"))
result = 0
while(n>0):
    ld = n % 10
    result = (result*10)+ld
    n //= 10

if(n == result):
    print("palidrom")

else:
    print("not palidrom")