"""
Paint Fill: Implement the "paint nil" function that one might see on many image editing programs.
That is, given a screen (represented by a two-dimensional array of colors), a point, and a new color,
nil in the surrounding area until the color changes from the original color.
Hints: #364, #382
"""


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        max_row = len(image)
        max_col = len(image[0])
        old_color = image[sr][sc]

        self.flood_fill_helper(image, sr, sc, max_row, max_col, newColor, old_color)
        return image

    def flood_fill_helper(self, image, x, y, max_row, max_col, color, old_color):
        """
        """
        if x < 0 or x >= max_row or y < 0 or y >= max_col or image[x][y] == color or image[x][y] != old_color:
            return

        image[x][y] = color
        self.flood_fill_helper(image, x + 1, y, max_row, max_col, color, old_color)
        self.flood_fill_helper(image, x - 1, y, max_row, max_col, color, old_color)
        self.flood_fill_helper(image, x, y + 1, max_row, max_col, color, old_color)
        self.flood_fill_helper(image, x, y - 1, max_row, max_col, color, old_color)