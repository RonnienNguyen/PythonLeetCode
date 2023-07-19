# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting adjacent
# lands horizontally or vertically. You may assume all four edges of the grid are
# all surrounded by water.
# Example 1:
# Input:
# 11110
# 11010
# 11000
# 00000
# Output: 1
# Example 2:
# Input:
# 11000
# 11000
# 00100
# 00011
# Output: 3

def numIslands(grid):
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            dfs(ni, nj)

    m = len(grid)
    if m == 0:
        return 0
    n = len(grid[0])
    ret = 0
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                ret += 1
                dfs(i, j)

    return ret

input_grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print(numIslands(input_grid))