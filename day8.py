# n = int(input("enter a number:"))
# nod = len(str(n))
# total = 0
# temp = n

# while(n>0):
#     ld = n % 10
#     total = total+(ld**nod)
#     n //= 10

# if(temp == total):
#     print("armstrong")
# else:
#     print("not")


# n = 10
# result = []
# for i in range(1,n+1):
#     if n% i == 0:
#         result.append(i)
# print(result)


from math import gcd,sqrt
a = 12
b = 6

result = []
n = gcd(a,b)

for i in range(1,int(sqrt(n)) + 1):
    if n %i == 0:
        result.append(i)
    if n// i != i:
        result.append(n// i)

result.sort()
print(result)