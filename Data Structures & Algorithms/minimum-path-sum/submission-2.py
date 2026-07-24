class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cache = {}

        def dfs(row,col):
            if (row,col) in cache:
                return cache[(row,col)]

            if row==rows-1 and col==cols-1:
                return grid[row][col]
            
            if row<0 or row>=rows or col<0 or col>=cols:
                return float("inf")
            
            ans = grid[row][col] + min(dfs(row+1,col), dfs(row,col+1))
            cache[(row,col)] = ans
            return ans
         
        return dfs(0,0)