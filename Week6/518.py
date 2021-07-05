class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.dic={}
        coins.sort()
        self.helpchange(amount,coins)
        return self.dic[(amount,tuple(coins))]
    def helpchange(self,amount,coins):
        if (amount,tuple(coins)) in self.dic:
            return self.dic[(amount,tuple(coins))]
        if len(coins)==0:
            if amount==0:
                res=1
            else:
                res=0
            self.dic[(amount,tuple(coins))]=res
            return res
        if len(coins)==1:
            if amount==0:
                res=1
            elif coins[0]>amount:
                res=0
            elif amount%coins[0]==0:
                res=1
            else:
                res=0
            self.dic[(amount,tuple(coins))]=res
            return res
        if coins[-1]>amount:
            self.dic[(amount,tuple(coins))]=self.helpchange(amount,coins[:-1])
            return self.dic[(amount,tuple(coins))]
        else:
            self.dic[(amount,tuple(coins))]=self.helpchange(amount,coins[:-1])+self.helpchange(amount-coins[-1],coins)
            return self.dic[(amount,tuple(coins))]