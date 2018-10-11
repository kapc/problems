#! /usr/env/python

"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotate_matrix(matrix):
    """
    """
    if not matrix:
        return matrix
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return matrix
    n = len(matrix)
    for layer in range(0, int(n/2)):
        first = layer
        last  = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            print(top)
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top




if __name__ == "__main__":
    matrix = [[1,2,3,4], [5,6,7,8], [7,8,9,10],[11,12,13,14]]
    rotate_matrix(matrix)
    print(matrix)

