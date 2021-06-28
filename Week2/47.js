var permuteUnique = function(nums) {
    nums.sort()
    var res=[]
    var visit=new Set()
     var permute=function(nums,idx,lst){
         if (idx==nums.length){res.push([...lst])}
         for (let i=0;i<nums.length;i++){
             if (i>0 && nums[i]==nums[i-1] && visit.has(i-1)) continue
             if (!visit.has(i)){
                 visit.add(i);
                 lst.push(nums[i])
                 permute(nums,idx+1,lst)
                 visit.delete(i)
                 lst.pop()
             }
         }
    }
    permute(nums,0,[])
    return res
};