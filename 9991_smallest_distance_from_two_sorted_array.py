a = [1, 5, 11, 23]
b = [3, 8, 9, 20, 25]

counter_a = 0
counter_b = 0

min_dist = float('inf')
min_pair = None

while (counter_a < len(a) and counter_b < len(b)):
    abs_diff = abs(a[counter_a] - b[counter_b])

    if (abs_diff < min_dist):
        min_dist = abs_diff
        min_pair = (a[counter_a], b[counter_b])

    if (a[counter_a] < b[counter_b]):
        counter_a += 1
    else:
        counter_b += 1

print(min_pair)