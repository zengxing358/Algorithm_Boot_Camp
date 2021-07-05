class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N=len(matrix)
        M=len(matrix[0])
        left=0
        right=N*M-1
        while left<=right:
            mid=(left+right)>>1
            x=mid//M
            y=mid%M
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]<target:
                left=mid+1
            else:
                right=mid-1
        return False
