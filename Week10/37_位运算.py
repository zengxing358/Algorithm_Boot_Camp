class Solution:
    def __init__(self):
        self.line=[1022]*9
        self.column=[1022]*9
        self.block=[1022]*9
        self.ones={}
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cnt=0
        self.grids=set()
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    cnt+=1
                    self.grids.add((i,j))
                else:
                    digit=int(board[i][j])
                    self.flip(i,j,digit)
        self.board=board
        self.dfs(cnt)
    def get(self,i,j):
        return self.line[i]&self.column[j]&self.block[i//3*3+j//3]
    def getcnt(self,state):
        if state in self.ones:
            return self.ones[state]
        res=0
        cur=state
        while state:
            state-=state&(-state)
            res+=1
        self.ones[cur]=res
        return res
    def dfs(self,cnt):
        if cnt==0:
            return True
        i=0
        j=0
        mincnt=10
        mask=0
        for x,y in self.grids:
            state=self.get(x,y)
            tc=self.getcnt(state)
            if tc==0:
                return False
            if tc<mincnt:
                i=x
                j=y
                mincnt = tc
                mask=state
                if tc==1:
                    break
        while mask:
            digitMask = mask & (-mask)
            digit = bin(digitMask).count("0") - 1
            self.flip(i,j,digit)
            self.board[i][j]=str(digit)
            self.grids.remove((i,j))
            if self.dfs(cnt-1):
                return True
            self.flip(i,j,digit)
            self.grids.add((i,j))
            mask-=mask & (-mask)
        return False
                
    def flip(self,i,j,digit):
        self.line[i]^=(1<<digit)
        self.column[j]^=(1<<digit)
        self.block[(i//3)*3+j//3]^=(1<<digit)