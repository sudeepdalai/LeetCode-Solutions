class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] == "0" or
                (r, c) in visited
            ):
                return

            visited.add((r, c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands
