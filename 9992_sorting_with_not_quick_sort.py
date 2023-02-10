import math

def not_quick_sort(arr, i, j):
    n = j - i + 1

    if (n == 2 and arr[i] > arr[j]):
        arr[i], arr[j] = arr[j], arr[i]
    elif (n > 2):
        m = math.ceil(2 * n / 3)
        not_quick_sort(arr, i, i + m-1)
        not_quick_sort(arr, i + n-m, i + n-1)
        not_quick_sort(arr, i, i + m-1)


arr = [6,5,4,3,2,1]
not_quick_sort(arr, 0, len(arr) - 1)
print(arr)