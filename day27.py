# 26. Remove Duplicates from Sorted Array

# Brute
nums = [0,0,1,1,1,2,2,3,3,4]

# n = len(nums)
# freq_map = {}

# for i in range(0,n):
#     freq_map[nums[i]] = 0

# j = 0
# for i in freq_map:
#     nums[j] = i
#     j += 1

# print(j)

#Optimal

n = len(nums)
def sorted(nums):
    if n == 1:
        return 1
    i = 0
    j = i+1
    while(j<n):
        if nums[j] != nums[i]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    return i+1

print(sorted(nums))

    

