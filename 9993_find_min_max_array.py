def min_max_array(arr):
    mid = len(arr) // 2

    if (len(arr) == 1):
        return (arr[0], arr[0])
    
    partition1_min, partition1_max = min_max_array(arr[:mid])
    partition2_min, partition2_max = min_max_array(arr[mid:])

    tmp_min = min(partition1_min, partition2_min)
    tmp_max = max(partition1_max, partition2_max)
    
    return (tmp_min, tmp_max)
     

print(min_max_array([4,3,2,5,1,6]))