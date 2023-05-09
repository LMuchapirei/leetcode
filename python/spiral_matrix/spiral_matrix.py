class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return
        m,n=len(matrix),len(matrix[0])
        res,count,ub1,ub2=[],1,n,m-1
        i,j,di,dj=0,0,0,1
        for k in range(m*n):
            res.append(matrix[i][j])
            if count == ub1:
                di,dj=dj,-di
                count,ub1,ub2=0,ub2,ub1-1
            count +=1
            i,j=i+di,j+dj
        return res