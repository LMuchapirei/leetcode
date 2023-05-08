class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        data=[]
        for i in range(len(mat)):
            data.append(mat[i][i])
        for i in range(len(mat)):
            if i==len(mat)-i-1:
                continue
            data.append(mat[i][len(mat)-i-1])
        return sum(data)
    
    #  Another way to solve this one
        # for i in range(len(mat)):
        #     # primary diagonal
        #     res += mat[i][i]
        #     # secondary diagonal
        #     res += mat[i][len(mat)-i-1]

        # if len(mat) % 2 !=0:
        #     mid = (len(mat)-1)//2
        #     res -= mat[mid][mid]
        # return res
    

