var searchRange = function(nums, target) {
    var res=[]
    left=0
    right=nums.length
    while(left<right){
        mid=parseInt((left+right)/2)
        if (nums[mid]>=target){
            right=mid
        }else{
            left=mid+1
        }
    }
    res.push(left)
    left=-1
    right=nums.length-1
    while (left<right){
        mid=parseInt((left+right+1)/2)
        if(nums[mid]<=target){
            left=mid
        }else{
            right=mid-1
        }
    }
    res.push(left)
    if (res[1]<res[0]){
        return [-1,-1]
    }
    return res
};