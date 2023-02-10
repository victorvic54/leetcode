n = int(input())
arr = []
highest = [[0] * n for i in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split(" "))))

xyz_direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
high_coor = set()

for i in range(n):
    for j in range(n):
        is_highest = True

        for path in range(len(xyz_direction)):
            dir_x, dir_y = xyz_direction[path]

            new_x = i + dir_x
            new_y = j + dir_y

            if (0 <= new_x < n and 0 <= new_y < n):
                if (arr[new_x][new_y] > arr[i][j]):
                    is_highest = False

        if (is_highest):
            highest[i][j] = 1
            high_coor.add((i, j))


xy_direction = [[0, -1], [0, 1], [-1, 0], [1, 0]]
tmp_arr = [[0] * n for i in range(n)]

while (len(high_coor) != 0):
    coor = high_coor.pop()
    x = coor[0]
    y = coor[1]

    queue = set()
    queue.add((x, y))

    while (len(queue) != 0):
        x, y = queue.pop()

        tmp_arr[x][y] = 1
        
        for path in range(len(xy_direction)):
            dir_x, dir_y = xy_direction[path]

            new_x = x + dir_x
            new_y = y + dir_y

            if (0 <= new_x < n and 0 <= new_y < n and arr[new_x][new_y]== arr[x][y] and (not tmp_arr[new_x][new_y])):
                queue.add((new_x, new_y))
                
                if ((new_x, new_y) in high_coor):
                    high_coor.remove((new_x, new_y))


zero_color_set = set()

for i in range(n):
    for j in range(n):
        if (tmp_arr[i][j] - highest[i][j] != 0):
            zero_color_set.add((i, j))


while (len(zero_color_set) != 0):
    coor = zero_color_set.pop()
    x = coor[0]
    y = coor[1]

    queue = set()
    queue.add((x, y))

    while (len(queue) != 0):
        x, y = queue.pop()

        tmp_arr[x][y] = 0
        
        for path in range(len(xyz_direction)):
            dir_x, dir_y = xyz_direction[path]

            new_x = x + dir_x
            new_y = y + dir_y

            if (0 <= new_x < n and 0 <= new_y < n and arr[new_x][new_y] == arr[x][y] and (tmp_arr[new_x][new_y])):
                queue.add((new_x, new_y))
                
                if ((new_x, new_y) in zero_color_set):
                    zero_color_set.remove((new_x, new_y))

print(tmp_arr)
