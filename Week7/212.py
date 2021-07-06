class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.tire={}
        self.board=board
        for word in words:
            root=self.tire
            for w in word:
                if w not in root:
                    root[w]={}
                root=root[w]
            root["#"]=True
        self.res=set()
        self.row=len(board)
        self.col=len(board[0])
        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] in self.tire:
                    self.dfs(i,j,self.tire[board[i][j]],board[i][j],{(i,j)})
        return list(self.res)
    def dfs(self,x,y,cur,s,visit):
        if "#" in cur:
            self.res.add(s)
        for i,j in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
            if i>=0 and i<self.row and j>=0 and j<self.col and self.board[i][j] in cur and (i,j) not in visit:
                self.dfs(i,j,cur[self.board[i][j]],s+self.board[i][j],visit|{(i,j)})