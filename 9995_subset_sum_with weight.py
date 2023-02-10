def subset_sum_with_weight(arr, total, weight, result):
    if (total < 0 or (arr == [] and total > 0)):
        return float('-inf')
    elif (total == 0):
        return result

    a = subset_sum_with_weight(arr[1:], total, weight[1:], result)
    b = subset_sum_with_weight(arr[1:], total - arr[0], weight[1:], result + weight[0])
    return max(a, b)


print(subset_sum_with_weight([4,6,9,14,8], 23, [1,2,3,4,5], 0))