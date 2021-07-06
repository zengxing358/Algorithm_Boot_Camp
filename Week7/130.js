var solve = function(board) {
    var visit=new Set();
    var row=board.length;
    var col=board[0].length;
    var bfs=function(x,y){
        for (let [x1,y1] of [[x+1,y],[x-1,y],[x,y-1],[x,y+1]]){
                if (x1>=0 && x1<row && y1>=0 && y1<col && board[x1][y1]=="O"){
                    var idx=x1*col+y1
                    if (!(visit.has(idx))){
                        visit.add(idx)
                        bfs(x1,y1)
                    }
                }
        }
    }
    for (var i of [0,row-1]){
        for (let j=0;j<col;j++){
            var idx=i*col+j
            if (board[i][j]=="O" && !(visit.has(idx))){
                visit.add(idx)
                bfs(i,j)
            }
        }
    }
    for (let i=0;i<row;i++){
        for (var j of [0,col-1]){
            var idx=i*col+j
            if (board[i][j]=="O" && !(visit.has(idx))){
                visit.add(idx)
                bfs(i,j)
            }
        }
    }
    for(let i=1;i<row-1;i++){
        for(let j=0;j<col-1;j++){
            var idx=i*col+j
            if (board[i][j]=="O" && !(visit.has(idx))){
                board[i][j]="X"
            }
        }
    }
};