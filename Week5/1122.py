class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic={}
        dicre={}
        L=len(arr2)
        for i in arr2:
            dic[i]=-L
            dicre[-L]=i
            L-=1
        for index,val in enumerate(arr1):
            if val in dic:
                arr1[index]=dic[val]
        arr1.sort()
        for index,val in enumerate(arr1):
            if val<0:
                arr1[index]=dicre[val]
        return arr1