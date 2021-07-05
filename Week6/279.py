class Solution:
    def numSquares(self, n: int) -> int:
        i=1
        self.temp=[]
        self.dic=set()
        while i*i<=n:
            self.temp.append(i*i)
            self.dic.add(i*i)
            i+=1
        queue=[[n,0]]
        self.temp=self.temp[::-1]
        while queue:
            rest,count=queue.pop(0)
            if rest in self.dic:
                return count+1
            for num in self.temp:
                if num<rest:
                    queue.append([rest-num,count+1])