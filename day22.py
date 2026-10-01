# merge sort

num = [2,3,1,7,8,29,4,0]   

def merge_num(left,right):

    result = []
    i,j = 0,0
    l,r = len(left),len(right)

    while(i<l and j<r):
        if (left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i<l:
        while i<l:
            result.append(left[i])
            i += 1

    else:
        while j<r:
            result.append(right[j])
            j += 1

    return result

    

def merge_sort(num):
    if len(num) <= 1:
        return num

    mid = len(num) // 2

    left_num = num[ : mid]
    right_num = num[mid : ]

    left = merge_sort(left_num)
    right = merge_sort(right_num)
    return merge_num(left,right) 

print(merge_sort(num)) 

