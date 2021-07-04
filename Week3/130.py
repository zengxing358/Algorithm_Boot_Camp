class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board and board[0]:
            n=len(board)
            m=len(board[0])
            dic={}
            start=[]
            for i in range(n):
                for j in range(m):
                    if board[i][j]=='O':
                        dic[(i,j)]=0
                        if i==0 or i==n-1 or j==0 or j==m-1:
                            start.append((i,j))
            for x,y in start:
                if (x,y) in dic:
                    dic.pop((x,y))
                queue=[(x,y)]
                while queue:
                    x,y=queue.pop(0)
                    for x1,y1 in [[x+1,y],[x-1,y],[x,y-1],[x,y+1]]:
                        if (x1,y1) in dic:
                            dic.pop((x1,y1))
                            queue.append((x1,y1))
            for (x2,y2) in dic:
                board[x2][y2]='X'
        