
# Q1. Frequency Count

# n = [1, 2, 2, 3, 1, 2, 4, 3]
# dict = {}

# method 1.
# for i in range(0,len(n)):
#     if n[i] in dict:
#         dict[n[i]] += 1
#     else:
#         dict[n[i]] = 1
# print(dict)

# method 2.
# for i in range(0,len(n)):
#     dict[n[i]] = dict.get(n[i],0)+1
# print(dict)




# Q2. Duplicate Check

arr = [10, 20, 30, 40, 20, 50]

set = set()

for i in range(len(arr)):
    if arr[i] in set:
      print("dublicate vale:",arr[i])
      break
    set.add(arr[i])
   