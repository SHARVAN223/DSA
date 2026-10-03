#  Q.find the second largest element
nums = [1, 8, 7, 56, 90]

# Brute
# nums.sort()
# n = len(nums)
# print(nums[n-2])

# Better

# largest = float("-inf")
# S_largest = float("-inf")

# n = len(nums)
# for i in range(0,n):
#     largest = max(largest,nums[i])
# for i in range(0,n):
#     if nums[i]>S_largest and nums[i] != largest:
#         S_largest = nums[i]
   
# print(S_largest)


# Optimal

# largest = float("-inf")
# S_largest = float("-inf")
# n = len(nums)

# for i in range(0,n):
#     if nums[i] > largest:
#         S_largest = largest
#         largest = nums[i]

#     elif nums[i] > S_largest and nums[i] != largest:
#         S_largest = nums[i]
# print(S_largest)



# Q.Find secon largest number and second smallest number
largest = float("-inf")
smallest = float("inf")
S_largest = float("-inf")
s_smallest = float("inf")
n = len(nums)

for i in range(0,n):
    largest = max(largest,nums[i])
    smallest = min(smallest,nums[i])

for i in range(0,n):
    if nums[i]>S_largest and nums[i] != largest:
        S_largest = nums[i]
    elif nums[i]<s_smallest and nums[i] != smallest:
        s_smallest = nums[i]

print(S_largest)
print(s_smallest)

