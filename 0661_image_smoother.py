class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        directions = [(-1,-1), (-1, 0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]
        for i in range(len(img)):
            for j in range(len(img[0])):
                count = 0
                total = 0
                for dir_x, dir_y in directions:
                    if 0 <= i + dir_x < len(img) and 0 <= j + dir_y < len(img[0]):
                        count += 1
                        total += img[i+dir_x][j+dir_y] % 256
                img[i][j] = (total // count) * 256 + img[i][j]
        
        for i in range(len(img)):
            for j in range(len(img[0])):
                img[i][j] = img[i][j] // 256
        
        return img

