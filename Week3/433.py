class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank=set(bank)
        if end not in bank:
            return -1
        res=0
        dic={"A":"CGT", "C":'AGT', "G":"ACT", "T":"ACG"}
        font_queue=[start]
        end_queue=[end]
        L=len(start)
        bank.add(start)
        while font_queue:
            res+=1
            next_queue=[]
            for node in font_queue:
                bank.remove(node)
                for i in range(L):
                    for item in dic[node[i]]:
                        temp=node[:i]+item+node[i+1:]
                        if temp in end_queue:
                            return res
                        if temp in bank:
                            next_queue.append(temp)
            font_queue=next_queue
            font_queue,end_queue=end_queue,font_queue
        return -1
