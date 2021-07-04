var findRedundantDirectedConnection = function(edges) {
    var degree={}
    var idx=-1
    for (let i=0;i<edges.length;i++){
        start=edges[i][0]
        end=edges[i][1]
        if (!(end in degree)){
            degree[end]=[]
        }else{
            idx=end
        }
        degree[end].push(i)
    }
    function check(idx){
        var parent=[];
        for (let i=0;i<edges.length+1;i++){
            parent[i]=i
        }
        for (let i=0;i<edges.length;i++){
            if (i!=idx){
                s=edges[i][0]
                e=edges[i][1]
                temp=e
                while (parent[e]!=e){
                    e=parent[e]
                    if (e==s){
                        return [s,temp]
                    }
                }
                parent[s]=e
            }
        }
    }
    if (idx==-1){
        return check(-1)
    }
    while (true){
        cur=degree[idx].pop()
        if (check(cur)==null){
            return edges[cur]
        }
    }
};