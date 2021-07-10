var solveSudoku = function(board) {
    var vrows={}
    var vcols={}
    var vidxs={}
    for(let i=0;i<9;i++){
        vrows[i]=new Set()
        vcols[i]=new Set()
        vidxs[i]=new Set()
    }
    visit={}
    graph={}
    var getindex=function(x,y){
        return x*9+y
    }
    var getpos=function(idx){
        return [parseInt(idx/9),idx%9]
    }
    var getgrid=function(x,y){
        return parseInt(x/3)*3+parseInt(y/3)
    }
    for(let i=0;i<9;i++){
        for(let j=0;j<9;j++){
            if(board[i][j]=="."){
                visit[getindex(i,j)]=0
            }else{
                vidxs[getgrid(i,j)].add(parseInt(board[i][j]))
                vrows[i].add(parseInt(board[i][j]))
                vcols[j].add(parseInt(board[i][j]))
            }
        }
    }
    for (let idx in visit){
        var lst=getpos(idx)
        var x=lst[0]
        var y=lst[1]
        graph[idx]=[]
        for(let i=1;i<=9;i++){
            if((vrows[x].has(i))||(vcols[y].has(i))||(vidxs[getgrid(x,y)].has(i))){
                continue
            }
            graph[idx].push(i)
        }
        visit[idx]=graph[idx].length
    }
    queue=Object.keys(visit).sort(function(a,b){return visit[a]-visit[b]})
    var dfs=function(queue){
        if(queue.length==0){
            return true
        }
        var lst=getpos(queue[0])
        var x=lst[0]
        var y=lst[1]
        for(let v of graph[queue[0]]){
            if ((vrows[x].has(v))||(vcols[y].has(v))||(vidxs[getgrid(x,y)].has(v))){
                continue
            }
            board[x][y]=`${v}`
            vidxs[getgrid(x,y)].add(v)
            vcols[y].add(v)
            vrows[x].add(v)
            if (dfs(queue.slice(1))){
                return true
            }
            else{
                vidxs[getgrid(x,y)].delete(v)
                vcols[y].delete(v)
                vrows[x].delete(v)
                board[x][y]='.'
            } 
        }
        return false
    }
    dfs(queue)
};