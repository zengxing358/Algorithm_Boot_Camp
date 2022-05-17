var moveZeroes = function(nums) {
    var n=0;
    for(i=0;i<nums.length;i++){
        if (nums[i]!=0){
            nums[n]=nums[i];
            n++;
        }
    }
    while (n<nums.length){
        nums[n]=0;
        n++;
    }
};