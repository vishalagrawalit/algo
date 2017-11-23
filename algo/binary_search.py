def BS(arr, x, l, r):
    arr.sort()
    while l<r:
        mid = l + (r-1)//2
        if arr[mid]==x:
            return 1
        elif arr[mid]>x:
            r = mid - 1
        else:
            l = mid + 1
    return 0

def BSI(arr, x, l, r):
    arr.sort()
    while l<r:
        mid = l + (r-1)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            r = mid - 1
        else:
            l = mid + 1
    return -1    
