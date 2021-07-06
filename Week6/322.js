var coinChange = function(coins, amount) {
    if(amount==0){
        return 0
    }
    var dp=[]
    for(let i=0;i<=amount;i++){
        dp[i]=Number.MAX_VALUE
    }
    dp[0]=0
    for(let coin of coins){
        for(let i=coin;i<=amount;i++){
            dp[i]=Math.min(dp[i],dp[i-coin]+1)
        }
    }
    if(dp[dp.length-1]>amount){
        return -1
    }
    return dp[dp.length-1]
};