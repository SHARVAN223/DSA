n = int(input("enter a number:"))
nod = len(str(n))
total = 0
temp = n

while(n>0):
    ld = n % 10
    total = total+(ld**nod)
    n //= 10

if(temp == total):
    print("armstrong")
else:
    print("not")