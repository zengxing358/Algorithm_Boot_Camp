class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res=[0]*n
        for (x,y,c) in bookings:
            res[x-1]+=c
            if y<n:
                res[y]-=c
        for i in range(1,n):
            res[i]+=res[i-1]
        return res