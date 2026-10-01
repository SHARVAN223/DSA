def func(n):
    if n == 1:
        return 1
    return n + func(n-1)

sum = func(5)
print(sum)


# def func(n):
#     if n == 1:
#         return 1
#     return n * func(n-1)

# sum = func(4)
# print(sum)




def func(sum,i,n):
    if i>n:
        print(sum)
        return
    return func(sum+i,i+1,n)

func(0,1,5)