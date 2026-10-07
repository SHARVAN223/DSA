# Q.Moves Zero
nums = [0,1,0,3,12]
n = len(nums)

#.Brute
temp = []
for i in range(0,n):
    if nums[i] != 0:
        temp.append(nums[i])

nz = len(temp)
for i in range(0,nz):
    nums[i] = temp[i]

for i in range(nz,n):
    nums[i] = 0

print(nums)




# for i in range(0,n):
#     if nums[i] == 0:
#         break
#     i += 1


# for j in range(i+1,n):
#     if nums[j] != 0:
#         nums[i],nums[j] = nums[j],nums[i]
#         i += 1
#     j += 1

# print(nums)
 