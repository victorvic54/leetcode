def count_inversion_unsorted_array(arr):
    mid = len(arr) // 2

    if (len(arr) == 1):
        return (0, arr)

    (tmp1, a) = count_inversion_unsorted_array(arr[:mid])
    (tmp2, b) = count_inversion_unsorted_array(arr[mid:])
    return (tmp1 + tmp2 + count_inversion(a, b), merge(a, b))


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


def merge(arr1, arr2):
    tmp = []
    counter_a = 0
    counter_b = 0

    while True:
        if (counter_a < len(arr1) and counter_b < len(arr2)):
            if (arr1[counter_a] < arr2[counter_b]):
                tmp.append(arr1[counter_a])
                counter_a += 1
            else:
                tmp.append(arr2[counter_b])
                counter_b += 1
        elif (counter_a < len(arr1)):
            return tmp + arr1[counter_a:]
        else:
            return tmp + arr2[counter_b:]


print(count_inversion_unsorted_array([1,3,8,9,2,4,5,9,10]))