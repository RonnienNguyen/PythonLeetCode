# A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

# The world is modeled as an m x n binary grid isInfected, where isInfected[i][j] == 0 represents uninfected cells, and isInfected[i][j] == 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

# Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There will never be a tie.

# Return the number of walls used to quarantine all the infected regions. If the world will become fully infected, return the number of walls used.
# Input: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
# Output: 13
# Explanation: The region on the left only builds two new walls.


class Solution:
    def containVirus(self, isInfected):
        m, n = len(isInfected), len(isInfected[0])

        def dfs(i, j, visited, nextInfected):
            if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
                if isInfected[i][j] == 2:
                    return 0
                if isInfected[i][j] == 0:
                    nextInfected.add((i, j))
                    return 1
                else:
                    visited.add((i, j))
                    return dfs(i - 1, j, visited, nextInfected) + dfs(i + 1, j, visited, nextInfected) + dfs(i, j - 1, visited, nextInfected) + dfs(i, j + 1, visited, nextInfected)
            else:
                return 0

        ans = 0
        while True:
            visited = set()
            all_next_infect = set()
            stop, walls = set(), 0

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in visited:
                        nextInfected = set()
                        a = dfs(i, j, visited, nextInfected)

                        if len(stop) < len(nextInfected):
                            all_next_infect = all_next_infect | stop
                            stop = nextInfected
                            walls = a
                            p, q = i, j
                        else:
                            all_next_infect = all_next_infect | nextInfected

            if not stop:
                break
            ans += walls

            def fun(p, q):
                if 0 <= p < m and 0 <= q < n and isInfected[p][q] == 1:
                    isInfected[p][q] = 2
                    fun(p + 1, q)
                    fun(p - 1, q)
                    fun(p, q - 1)
                    fun(p, q + 1)

            fun(p, q)

            for a, b in all_next_infect:
                isInfected[a][b] = 1

        return ans

# Example usage:
isInfected = [[1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0, 0]]
solution = Solution()
result = solution.containVirus(isInfected)
print(result)  # Output: 13
