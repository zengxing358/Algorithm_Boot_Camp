class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times=times
        self.right=len(times)-1
        self.lst=[]
        dic={}
        maxnum=0
        for person in persons:
            dic[person]=dic.get(person,0)+1
            if dic[person]>=maxnum:
                maxnum=dic[person]
                self.lst.append(person)
            else:
                self.lst.append(self.lst[-1])

    def q(self, t: int) -> int:
        left=0
        right=self.right
        while left<right:
            mid=(left+right+1)//2
            if self.times[mid]<=t:
                left=mid
            else:
                right=mid-1
        return self.lst[left]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)