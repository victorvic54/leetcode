n = int(input())
arr = []
highest = [[0] * n for i in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split(" "))))

highest_point = []

for i in range(n):
    for j in range(n):
        is_highest = True

        if (i != 0):
            if (arr[i][j] <= arr[i-1][j]):
                is_highest = False

        if (i != len(arr) - 1):
            if (arr[i][j] <= arr[i+1][j]):
                is_highest = False
        
        if (j != 0):
            if (arr[i][j] <= arr[i][j-1]):
                is_highest = False

        if (j != len(arr[0]) - 1):
            if (arr[i][j] <= arr[i][j+1]):
                is_highest = False

        if (is_highest):
            highest[i][j] = 1
            highest_point.append((i, j))


result_arr = [[0] * n for i in range(n)]
direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


for i in range(len(highest_point)):
    x, y = highest_point[i]

    queue = set()
    queue.add((x, y))
    
    tmp_arr = [[0] * n for i in range(n)]
    
    while len(queue) != 0:
        x, y = queue.pop()

        tmp_arr[x][y] = 1
        
        for path in range(len(direction)):
            dir_x, dir_y = direction[path]

            new_x = x + dir_x
            new_y = y + dir_y

            if (0 <= new_x < n and 0 <= new_y < n and arr[new_x][new_y] < arr[x][y] and (not tmp_arr[new_x][new_y])):
                queue.add((new_x, new_y))

    print(tmp_arr)