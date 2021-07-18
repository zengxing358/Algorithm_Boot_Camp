var jump = function(nums) {
    if (nums.length==1){
        return 0
    }
    var left=0
    var right=nums[0]
    var res=0
    while (true){
        if(nums[left]==0){
            return -1
        }
        res+=1
        if (right>=nums.length-1){
            return res
        }
        var temp=0
        var nex=left
        for(let j=left+1;j<=right;j++){
            if (j+nums[j]>temp){
                temp=j+nums[j]
                nex=j
            }
        }
        left=nex
        right=temp
    }
};