# Q1.   arr = [10, 20, 10, 30, 20, 10, 40]  
# freqeucy count   

# dict = {}

# for i in range(0,len(arr)):
#     if arr[i] in dict:
#         dict[arr[i]] += 1
#     else:
#         dict[arr[i]] = 1
        
# print(dict)


#Optimal
# for i in range(0,len(arr)):  or
# for i in arr:
#     dict[i] = dict.get(i,0)+1
# print(dict)



# Q.Dupicate
# arr = [1, 2, 3, 2, 4, 1, 5, 2]


# dict = {}
# for i in arr:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1

# for i in dict:
#     if dict[i] > 1:
#         print(i)



# x  = set()
# duplicate = set()

# for i in arr:
#     if i in x:
#         duplicate.add(i)
#     else:
#         x.add(i)
# print(duplicate)



# Question 2: First Non-Repeating Element
# arr = [4, 5, 1, 2, 1, 4, 5]

# dict = {}
# for i in arr:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1

# for i in dict:
#     if dict[i] == 1:
#         print(i)


# Question: First duplicte element find 
arr = [10, 20, 10, 30, 20, 40, 30, 50]

dupli = set()

for i in arr:
    if i in dupli:
        print(i)
        break
    dupli.add(i)



    
