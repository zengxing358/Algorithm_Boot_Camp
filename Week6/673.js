var findNumberOfLIS = function(nums) {
    var n=nums.length
    if(n==1) return 1
    var dp=new Array(n)
    var count=new Array(n)
    var max_=0
    dp[0]=1
    count[0]=1
    for (let i=1;i<n;i++){
        dp[i]=1
        count[i]=1
        for (let j=0;j<i;j++){
            if(nums[i]>nums[j]){
               if(dp[i]==dp[j]+1) {
                   count[i]+=count[j]
               }else if (dp[j] + 1 > dp[i]){
                   dp[i] = dp[j] + 1
                    count[i] = count[j]
               }
        }
        }
        max_=Math.max(max_,dp[i])
    }
    var res=0
    for(let i=0;i<n;i++){
        if(dp[i]==max_){
            res+=count[i]
        }
    }
    return res
};