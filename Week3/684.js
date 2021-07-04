/**
 * @param {number[][]} edges
 * @return {number[]}
 */
 var findRedundantConnection = function(edges) {
    var graph={}
    var res=[]
    var dfs=(item,father)=>{
        var key=item.toString()
        for (var nx of graph[key]){
            if (nx!=father){
                if (visit.has(nx)){
                    return true
                }else{
                    visit.add(nx)
                    if (dfs(nx,item)) return true
                }
            }
        }
        return false
    }
    for (var [s,e] of edges){
        if (s in graph){
            graph[s].push(e)
        }else{
            graph[s]=[]
            graph[s].push(e)
        }
        if (e in graph){
            graph[e].push(s)
        }else{
            graph[e]=[]
            graph[e].push(s)
        }
        var visit=new Set()
        visit.add(s)
        if (dfs(s,-1)){
            return [s,e]
        }
    }
    return res
};