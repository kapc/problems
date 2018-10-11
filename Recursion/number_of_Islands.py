#! /usr/env/python

"""
Number of Distinct Islands
Difficulty:Medium

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution(object):
    def numDistinctIslands(self, grid):
        seen = set()
        def explore(r, c, r0, c0):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.add((r - r0, c - c0))
                explore(r+1, c, r0, c0)
                explore(r-1, c, r0, c0)
                explore(r, c+1, r0, c0)
                explore(r, c-1, r0, c0)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = set()
                explore(r, c, r, c)
                if shape:
                    shapes.add(frozenset(shape))
        return len(shapes)


def numDistinctIslands(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    max_row = len(grid)
    max_col = len(grid[0])
    visited = [[0 for i in xrange(max_col)] for j in xrange(max_row)]
    islands = 0
    list_islands = []
    seen = set()

    def visit_island(self, grid, i, j, x, y, max_row, max_col, visited):
        """
        Visit an island.
        """
        if i >= max_row or i < 0 or j >= max_col or j < 0 or visited[i][j] == 1 or grid[i][j] == 0:
            return

        visited[i][j] = 1

        self.visit_island(grid, i, j + 1, max_row, max_col, visited)
        self.visit_island(grid, i + 1, j, max_row, max_col, visited)
        self.visit_island(grid, i, j - 1, max_row, max_col, visited)
        self.visit_island(grid, i - 1, j, max_row, max_col, visited)

    for i in range(0, max_row):
        for j in range(0, max_col):
            if grid[i][j] == 1 and visited[i][j] == 0:
                self.visit_island(grid, i, j, x, y, max_row, max_col, visited)
                list_islands.append((i, j))
                islands += 1

