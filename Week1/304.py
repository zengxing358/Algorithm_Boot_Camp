class NumMatrix:
    
    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.N=len(matrix)
        if matrix:
            self.M=len(matrix[0])
            for i in range(self.N):
                for j in range(self.M):
                    if i!=0 and j!=0:
                        matrix[i][j]+=(matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1])
                    elif i!=0 and j==0:
                        matrix[i][j]+=matrix[i-1][j]
                    elif i==0 and j!=0:
                        matrix[i][j]+=matrix[i][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.getmatrix(row2,col2)+self.getmatrix(row1-1,col1-1)-self.getmatrix(row2,col1-1)-self.getmatrix(row1-1,col2)

    def getmatrix(self,row,col):
        if row<0:
            return 0
        if col<0:
            return 0
        if row>=self.N:
            row=self.N-1
        if col>=self.M:
            col=self.M-1
        return self.matrix[row][col]