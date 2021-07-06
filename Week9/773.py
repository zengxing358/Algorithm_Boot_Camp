class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        if board==[[1,2,3],[4,5,0]]:
            return 0
        vistit={}
        queue=[tuple(tuple(i) for i in board)]
        vistit[queue[0]]=0
        while queue:
            cur=queue.pop(0)
            s=0
            for i in range(6):
                if cur[i//3][i%3]==0:
                    break
                s+=1
            nextboard=[]
            curboard=[list(i) for i in cur]
            for x,y in [[s//3-1,s%3],[s//3+1,s%3],[s//3,s%3+1],[s//3,s%3-1]]:
                if x>=0 and x<2 and y>=0 and y<3:
                    curboard[s//3][s%3],curboard[x][y]=curboard[x][y],curboard[s//3][s%3]
                    nextboard.append(tuple(tuple(i) for i in curboard))
                    curboard[s//3][s%3],curboard[x][y]=curboard[x][y],curboard[s//3][s%3]
            for nextbd in nextboard:
                if nextbd not in vistit:
                    vistit[nextbd]=vistit[cur]+1
                    if nextbd==((1,2,3),(4,5,0)):
                        return vistit[nextbd]
                    queue.append(nextbd)
        return -1