n = int(input())
arr = []
highest = [[0] * n for i in range(n)]

for i in range(n):
    arr.append(list(map(int, input().split(" "))))

direction = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for i in range(n):
    for j in range(n):
        is_highest = True

        for path in range(len(direction)):
            dir_x, dir_y = direction[path]

            new_x = i + dir_x
            new_y = j + dir_y

            if (0 <= new_x < n and 0 <= new_y < n):
                if (arr[new_x][new_y] > arr[i][j]):
                    is_highest = False

        if (is_highest):
            highest[i][j] = 1

print(highest)

        

