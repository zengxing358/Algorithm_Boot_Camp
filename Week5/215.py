class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        rk=n-k
        def quicksort(arr,start,end):
            if start<end:
                r=random.randint(start,end-1)
                arr[start],arr[r]=arr[r],arr[start]
                s=arr[start]
                cur=start+1
                right=end
                mid=start
                while cur<right:
                    if arr[cur]<s:
                        mid+=1
                        arr[cur],arr[mid]=arr[mid],arr[cur]
                        cur+=1
                    elif arr[cur]==s:
                        cur+=1
                    else:
                        right-=1
                        arr[cur],arr[right]=arr[right],arr[cur]
                arr[mid],arr[start]=arr[start],arr[mid]
                if rk<mid: 
                    return quicksort(arr,start,mid)
                elif rk>=right:
                    return quicksort(arr,right,end)
                return arr[mid]
        return quicksort(nums,0,len(nums))