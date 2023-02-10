def count_inversion(arr1, arr2):
    tmp = 0
    result = 0
    tmp_b = 0

    for i in range(len(arr1)):
        while (tmp_b < len(arr2) and arr1[i] > arr2[tmp_b]):
            tmp_b += 1
            tmp += 1

        result += tmp

    return result

print(count_inversion([1,3,8,9], [2,4,5,9,10]))