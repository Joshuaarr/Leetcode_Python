class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()

        def helper(x, y):
            if (
                x < 0 or 
                x >= len(grid) or
                y < 0 or 
                y >= len(grid[0]) or
                (x, y) in visited or
                grid[x][y] == 0
                ):
                return 0
            
            visited.add((x, y))
            
            return 1 + helper(x + 1, y) + helper(x - 1, y) + helper(x, y + 1) + helper(x, y - 1)
        

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]:
                    res = max(res, helper(x, y))
        return res
