class Solution {
    public Map<Integer,List<String>> map=new HashMap<Integer,List<String>>();
    public List<String> generateParenthesis(int n) {
        if (map.containsKey(n)) return map.get(n);
        List<String> res = new ArrayList<String>();
        if (n==0){
            res.add("");
        }else{
        for(int k=1;k<=n;k++){
            for (String i:generateParenthesis(k-1)){
                for (String j:generateParenthesis(n-k)){
                    res.add("("+i+")"+j);
                }
            }
        }}
        map.put(n, res);
        return res;
    }
}