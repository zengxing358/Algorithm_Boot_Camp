var myPow = function(x, n) {
    var quick=function(x,n){
        var cur=x
        var res=1
        while (n>0){
            if(n&1==1){
                res*=cur
            }
            cur*=cur
            n=n/2
        }
        return res
    }
    return n>=0?quick(x,n):1/quick(x,n*-1)
};