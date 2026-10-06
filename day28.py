# Q.Right rotate array by 1 place

nums = [2,37,382,29,1,78]
n = len(nums)
# A. nums[:] = [nums[n-1]] + nums[0:n-1]
# print(nums)

# B.
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1] = nums[i]
nums[0] = temp

print(nums)