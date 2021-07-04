var canFinish = function(numCourses, prerequisites) {
    var visit={}
    for(let i=0;i<numCourses;i++){
        visit[i]=0
    }
    graph={}
    for ([a,b] of prerequisites){
        if (b in graph){
            graph[b].push(a)
        }else{
            graph[b]=[]
            graph[b].push(a)
        }
    }
    var bfs=(node)=>{
        visit[node]=1
        if (node in graph){
            for (var nx of graph[node]){
                        if (visit[nx]==0){
                            if (bfs(nx)){
                                return true
                            }
                        }else if(visit[nx]==1){
                            return true
                        }
                    }
        }
        visit[node]=2
        return false
    }
    for(let i=0;i<numCourses;i++){
        if (visit[i]==0){
            if (bfs(i)){
                return false
            }
        }
    }
    return true
};