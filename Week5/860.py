class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hand={5:0,10:0}
        while len(bills):
            money=bills.pop(0)
            if money==5:
                hand[5]+=1
            elif money==10:
                if hand[5]:
                    hand[5]-=1
                    hand[10]+=1
                else:
                    return False
            else:
                if hand[5] and hand[10]:
                    hand[5]-=1
                    hand[10]-=1
                elif hand[5]>=3:
                    hand[5]-=3
                else:
                    return False
        return True