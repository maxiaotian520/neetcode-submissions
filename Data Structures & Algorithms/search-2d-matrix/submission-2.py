class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 这道题的重点前提就是，r是从第一行开始，c是从最后一列开始，优先顶下顺序，后面就免了在行和列之间的多重二分
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n-1  # this two premise are important premise, they help the following steps
        while r < m and c >= 0:
            if matrix[r][c] > target:  # based on r, c = 0, n-1
                c -= 1
            elif matrix[r][c] < target: # based on r, c = 0, n-1
                r += 1
            else:
                return True
        return False


