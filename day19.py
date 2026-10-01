# Selection sort

nums = [7,3,9,2,8,4,1]

def selectionSort(nums):
    n = len(nums)
    for i in range(0,n):
        min_index = i

        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i] , nums[min_index] = nums[min_index] , nums[i]

    return nums


print(selectionSort(nums))
            