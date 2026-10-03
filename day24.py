#  find the largest element
nums = [1, 8, 7, 56, 90]

largest = nums[0]
n = len(nums)
for i in range(0,n):
    largest = max(largest,nums[i])

print(largest)

