"""
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
"""


class Solution(object):
    def get_length(self, M, row, col, num_rows, num_cols, visited, dir_x, dir_y, idx):
        length = 0
        if visited[row][col][idx]:
            return length
        while col < num_cols and row < num_rows and M[row][col] == 1:
            visited[row][col][idx] = True
            length += 1
            col += dir_y
            row += dir_x
        return length

    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        num_rows = len(M)
        num_cols = len(M[0])
        visited = [[[False, False, False, False] for x in xrange(num_cols)] for y in xrange(num_rows)]
        max_len = 0

        for row in range(0, num_rows):
            for col in range(0, num_cols):
                max_len = max(max_len, self.get_length(M, row, col, num_rows, num_cols, visited, 0, 1, 0))
                max_len = max(max_len, self.get_length(M, row, col, num_rows, num_cols, visited, 1, 0, 1))
                max_len = max(max_len, self.get_length(M, row, col, num_rows, num_cols, visited, 1, 1, 2))
                max_len = max(max_len, self.get_length(M, row, col, num_rows, num_cols, visited, 1, -1, 3))
        return max_len

"""
DP solution.
"""


class Solution(object):

    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M:
            return 0
        num_rows = len(M)
        num_cols = len(M[0])
        dp = [[[0, 0, 0, 0] for _ in xrange(num_cols)] for _ in xrange(num_rows)]
        max_count = 0

        for row in range(0, num_rows):
            for col in range(0, num_cols):
                if M[row][col] == 1:
                    dp[row][col][0] = 1 if col <= 0 else dp[row][col - 1][0] + 1
                    dp[row][col][1] = 1 if row <= 0 else dp[row - 1][col][1] + 1
                    dp[row][col][2] = 1 if row <= 0 or col <= 0 else dp[row - 1][col - 1][2] + 1
                    dp[row][col][3] = 1 if row <= 0 or col >= num_cols - 1 else dp[row - 1][col + 1][3] + 1
                    max_count = max(max_count, max(dp[row][col]))
        return max_count
