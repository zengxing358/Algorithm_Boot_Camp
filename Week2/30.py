class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n=len(words)
        m=len(words[0])
        L=m*n
        res=[]
        ls=len(s)
        dicw={}
        for word in words:
            dicw[word]=dicw.get(word,0)+1
        for i in range(m):
            left=i
            right=i
            cnt=0
            dics={}
            while left+L<=ls:
                w=s[right:right+m]
                right+=m
                if w not in dicw:
                    left=right
                    dics.clear()
                    cnt=0
                else:
                    dics[w]=dics.get(w,0)+1
                    cnt+=1
                    while dics[w]>dicw[w]:
                        dw=s[left:left+m]
                        left+=m
                        dics[dw]-=1
                        cnt-=1
                    if cnt==n:
                        res.append(left)
        return res