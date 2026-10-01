num = [4,1,7,9,8,6]
n = len(num)

def partition(num,low,high):
    pivot = num[low]
    i=low
    j=high
    while i<j:
        while(i<=high-1 and num[i] <= pivot):
            i += 1
        while(j>= low+1 and num[j] > pivot):
            j -= 1
        if(i<j):
            num[i],num[j] = num[j],num[i]
    num[low] , num[j] = num[j], num[low]
    return j

def quick_sort(num,low,high):
    
    if(low<high):
        p_index = partition(num,low,high)
        quick_sort(num,low,p_index-1)
        quick_sort(num,p_index+1,high)
    return num

print(quick_sort(num,0,n-1))