def FS(arr, x):
    arr.sort()
    n = len(arr)
    if (x>=arr[n-1]):
        return 1
    if (x<arr[0]):
        return 0
    for i in range(1, n):
        if arr[i]>x:
            return 1

    return 0

def FSI(arr, x):
    arr.sort()
    n = len(arr)
    if (x>=arr[n-1]):
        return n-1
    if (x<arr[0]):
        return -1
    for i in range(1, n):
        if arr[i]>x:
            return i-1

    return -1
