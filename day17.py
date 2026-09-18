# Q.Check palidrom using loop

# s = "NITkN"
# n = len(s)

# left = 0
# right = n-1

# is_palindrom = True
# while(left < right):
#     if s[left] != s[right]:
#         is_palindrom = False
#         break
#     left += 1
#     right -= 1

# if is_palindrom:
#     print("plaidrom")

# else:
#     print("not palidrom")


# Q.Check palidrom using Func

# def func(s):
#     n = len(s)
#     left = 0
#     right = n-1

#     while(left <= right):
#         if s[left] != s[right]:
#             return False
#         left +=1
#         right += 1
#     return True


# print(func("sharvan"))

s = "nitkn"

def func(s,left , right):
    if left >= right:
        print("palidrom")
        return
      
    if s[left] != s[right]:
        print("not")
        return 

    return func(s,left+1,right-1)


func(s,0,len(s)-1)







