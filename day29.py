# right rotate array by k places
nums = [1,2,3,4,5,6,7]
k = 3

#Brute
# n = len(nums)
# rotation = n%k
# for _ in range(0,rotation):
#     e = nums.pop()
#     nums.insert(0,e)
# print(nums)

#Better
# n = len(nums)
# nums[:] = nums[n-k: ] + nums[0:n-k]
# print(nums)

#Optimal
n = len(nums)

def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1

reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n-1)

print(nums)

