# /usr/env/python

"""
1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""

def zero_matrix(matrix):
    """

    :param matrix:
    :return:
    """
    rows = []
    colums = []


    def zero_row(row):
        col_size = len(matrix[0])
        for i in range(0, col_size):
            matrix[row][i] = 0

    def zero_col(col):
        row_size = len(matrix)
        for i in range(0, row_size):
            matrix[i][col] = 0

    if not matrix:
        return matrix
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                rows.append(i)
                colums.append(j)

    for row in rows:
        zero_row(row)

    for col in colums:
        zero_col(col)


if __name__ == "__main__":
    matrix = [[1,2,4,5,6], [1,2,4,3,4], [1,2,0,2,3]]
    zero_matrix(matrix)
    print(matrix)
