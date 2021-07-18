var merge = function(intervals) {
    var res=[]
    var dic=[]
    for ([left,right] of intervals){
        dic.push([left,1])
        dic.push([right,-1])
    }
    var cnt=0
    function f(a,b){
            if(a[0]==b[0]){
                return b[1]-a[1]
            }
            return a[0]-b[0]
        }
    dic.sort(f)
    for([l,i] of dic){
        if (cnt==0){
            res.push([l])
        }
        cnt+=i
        if (cnt==0){
            res[res.length-1].push(l)
        }
    }
    return res
};