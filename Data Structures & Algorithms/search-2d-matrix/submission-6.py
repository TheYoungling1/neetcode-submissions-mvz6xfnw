class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # brute force solution m * n
        # so we know that the value to the diagonal right of a square is always bigger than that squaress values


        # first integer of every row > the last integer of the prev row
        # can be treated as one array, but  collapsing takes O(m*n) 
        # times

        left = 0
        m = len(matrix)
        n = len(matrix[0])
        right = m * n - 1 # right corner element
        print(right)

        while left <= right:
            mid = (right + left) // 2
            print(mid)
            # knowing the index of mid, we can devide by 4 
            # quotient is the row, remainder is the col
            mid_row = mid // n
            mid_col = mid - (mid_row * n)

            print(mid_row, mid_col)
            if target > matrix[mid_row][mid_col]:
                left = mid + 1
            elif target < matrix[mid_row][mid_col]:
                right = mid - 1
            else:
                return True

        return False 