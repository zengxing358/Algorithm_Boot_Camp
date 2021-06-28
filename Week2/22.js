var map={0:[""]}
var generateParenthesis = function(n) {
    if (n in map){
        return map[n];
    }
    if (n==0){
        return [""];
    }
    var res=[]
    for(let k = 1; k<=n; k++){
        var a=generateParenthesis(k-1)
        var b=generateParenthesis(n-k)
        for (const i of a){
            for (const j of b){
                res.push(`(${i})${j}`)
            }
        }
    }
    map[n]=res
    return res
};