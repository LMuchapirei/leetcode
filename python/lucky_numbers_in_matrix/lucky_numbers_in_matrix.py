class Solution:
    def luckyNumbers (self, matrix):
        #  [
        #   [3,7,8], (0,0). get elements in row and element in columns if min(rows) == min( colums) return the element that satisfies such a condition
        #   [9,11,13],
        #   [15,16,17]
        # ]
        # row by columns
        # given an index [i,j[]
        # [ [3,7,8],
        #   [9,11,13],
        #   [15,16,17]
        # ]
        ## solution of this complexity is O(N*M) where M and N are the number of rows and columns in the matrix
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                rows,columns = self.get_row_and_column_elements(matrix, i, j)
                if min(rows) == max(columns):
                    ans.append(min(rows))
    def get_row_and_column_elements(self,matrix, i, j):
        m = len(matrix)
        # Get all elements in the same row
        row_elements = matrix[i]
        # Get all elements in the same column
        column_elements = [matrix[x][j] for x in range(m)]
        
        return row_elements, column_elements
    
s =Solution()
val = s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])
print(val)