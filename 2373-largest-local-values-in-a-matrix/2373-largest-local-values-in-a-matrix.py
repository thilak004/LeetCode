class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0]*(n-2) for i in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                maxi=0
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        maxi = max(maxi,grid[r][c])
                res[i][j] = maxi
        return res