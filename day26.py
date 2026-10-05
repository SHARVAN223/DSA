# check if array sorted 
nums = [1,2,3,4,8,9,10]

n = len(nums)
def sorted(nums):
    for i in range(0,n-1):
        if nums[i] > nums[i+1]:
            return False
    return True

print(sorted(nums))
    