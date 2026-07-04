class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeros.add((r, c))
        
        for r, c in zeros:
            #top
            for i in range(c - 1, -1, -1):
                matrix[r][i] = 0
            #down
            for i in range(c + 1, len(matrix[0])):
                matrix[r][i] = 0
            #right
            for i in range(r + 1, len(matrix)):
                matrix[i][c] = 0
            #left
            for i in range(r - 1, -1, -1):
                matrix[i][c] = 0

