class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        queue=[(0,0)]
        deep=0
        visit={(0,0)}
        while queue:
            temp=[]
            for m1,n1 in queue:
                while m1<m and n1<n and word1[m1]==word2[n1]:
                    m1+=1
                    n1+=1
                if m1==m and n1==n:
                    return deep
                if m1<m and (m1+1,n1) not in visit:
                    temp.append((m1+1,n1))
                    visit.add((m1+1,n1))
                if n1<n and (m1,n1+1) not in visit:
                    temp.append((m1,n1+1))
                    visit.add((m1,n1+1))
                if n1<n and m1<m and (m1+1,n1+1) not in visit:
                    temp.append((m1+1,n1+1))
                    visit.add((m1+1,n1+1))
            deep+=1
            queue=temp


