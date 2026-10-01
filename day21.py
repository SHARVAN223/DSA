# Insertion sort

num = [10,4,5,8,15,1,3] 

n = len(num)
for i in range(1,n):
    key = num[i]
    j = i-1

    while(j>=0 and num[j] > key):
        num[j+1] = num[j]
        j -= 1

    num[j+1] = key
    print(num)

print("exact anser:",num)