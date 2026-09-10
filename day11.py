# Q1.
# BruteApproch

# n = [5,7,9,2,4,7,2,7,8,2,10]
# m = [10,111,9,6,3,2,4,5]

# for i in m:
#     count = 0
#     for j in n:
#         if j == i:      
#             count +=1
#     print(i,":",count)



# Optimal

# hash_list = [0]*11
# for num in n:
#     hash_list[num] += 1

# for num in m:
#     if num<1 or num>10:
#         print(0)
#     else:
#         print(num,":",hash_list[num])



# Dict me krna 
# hash_dict = {}
# for i in range(0,len(n)):
#     if n[i] in hash_dict:
#         hash_dict[n[i]] += 1
#     else :
#         hash_dict[n[i]] = 1

# for num in m:
#     if num<1 or num>10:
#         print(0)
#     else:
#         print(num,":",hash_dict.get(num,0))

# for j in range(0,len(m)):
#     if m[j] <1 or m[j] > 10:
#         print(0)
#     else:
#         print(m[j],":",hash_dict.get(m[j],0))


# Q.Character Hashing

s = "azyxyyzaaaa"
q = ["d","a","y","x"]


for ch in q:
    count = 0
    for cha in s:
        if cha == ch:
            count +=1

    print(ch,":",count)




