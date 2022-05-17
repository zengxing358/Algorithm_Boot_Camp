var removeDuplicates = function(nums) {
    var n=0;
    for(let j = 0; j < nums.length; j++){
        if (j==0 || nums[j]!=nums[j-1]){
            nums[n]=nums[j];
            n++;
        }
    }
    return n
};