class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic={}
        for cpdomain in cpdomains:
            num,com=cpdomain.split()
            while True:
                dic[com]=dic.get(com,0)+int(num)
                if '.' not in com:
                    break
                else:
                    com='.'.join(com.split('.')[1:])
        result=[]
        for key,value in dic.items():
            result.append(str(value)+' '+key)
        return result