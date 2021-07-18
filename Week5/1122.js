var relativeSortArray = function(arr1, arr2) {
    var arr=[]
    var dic={}
    for (i of arr1){
        dic[i]=(dic[i]==undefined?0:dic[i])+1
    }
    cnt=0
    for (j of arr2){
        if(j in dic){
            while(dic[j]!=0){
                arr[cnt++]=j
                dic[j]--
            }
            delete dic[j]
        }
    }
    for (let i in dic){
        while(dic[i]!=0){
            arr[cnt++]=i.valueOf()
            dic[i]--
        }
    }
    return arr
};