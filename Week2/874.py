class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dic=set()
        for x,y in obstacles:
            dic.add(self.hash(x,y))
        sx=0
        sy=0
        res=0
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        dir=0
        for command in commands:
            if command>0:
                for i in range(command):
                    nx=sx+dx[dir]
                    ny=sy+dy[dir]
                    if self.hash(nx,ny) in dic:
                        break
                    sx=nx
                    sy=ny
                res=max(sx*sx+sy*sy,res)
            elif command==-1:
                dir=(dir+1)%4
            else:
                dir=(dir+3)%4
        return res

    def hash(self,x,y):
        return (x+30000)*60000+y+30000