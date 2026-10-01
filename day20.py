# Q.Worest Case in bubble sort
nums = [1,2,3,4,5,6]

n = len(nums)

for i in range(n-2,-1,-1):
    
    for j in range(0,i+1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1],nums[j]




def fun(nums):
    n = len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1],nums[j]
    return nums


print(fun(nums))




# Q.Average Case
nums = [1, 2, 3, 4, 5]

n = len(nums)

for i in range(n - 2, -1, -1):

    is_swap = False

    for j in range(0, i + 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            is_swap = True

    if is_swap == False:
        print("Already sorted")
        break

print(nums)

    
    

