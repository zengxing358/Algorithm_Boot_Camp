class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lstn=[set() for _ in range(9)]
        lstm=[set() for _ in range(9)]
        lsti=[set() for _ in range(9)]
        visit={}
        graph={}
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    visit[(i,j)]=0
                else:
                    lsti[i//3*3+j//3].add(board[i][j])
                    lstm[j].add(board[i][j])
                    lstn[i].add(board[i][j])
        for x,y in visit:
            graph[(x,y)]={str(i) for i in range(1,10)}-(lsti[x//3*3+y//3]|lstm[y]|lstn[x])
            visit[(x,y)]=len(graph[(x,y)])
        queue=sorted(visit,key=visit.get)
        def dijs(queue):
            if not queue:
                return True
            x,y=queue[0]
            for v in graph[(x,y)]:
                if v not in lsti[x//3*3+y//3]|lstm[y]|lstn[x]:
                    board[x][y]=v
                    lsti[x//3*3+y//3].add(v)
                    lstm[y].add(v)
                    lstn[x].add(v)
                    if dijs(queue[1:]):
                        return True
                    else:
                        lsti[x//3*3+y//3].remove(v)
                        lstm[y].remove(v)
                        lstn[x].remove(v)
                        board[x][y]='.'
            return False
        dijs(queue)
