n = [1,2,3,4,2,13,3]
dict = {}


# method 1.
# for i in range(0,len(n)):
#     if n[i] in dict:
#         dict[n[i]] +=1
#     else:
#         dict[n[i]] =1
# print(dict)

# method 2.

for i in range(0,len(n)):
   dict[n[i]] = dict.get(n[i],0)+1
print(dict)
    

    