class Solution {
    private Map<String,List<String>> map=new HashMap<String,List<String>>();
    public List<List<String>> groupAnagrams(String[] strs) {
        for(String s:strs){
            char[] ch = s.toCharArray();
            Arrays.sort(ch);
            String hash=new String(ch);
            List<String> list = map.getOrDefault(hash, new ArrayList<String>());
            list.add(s);
            map.put(hash, list);
        }
        return new ArrayList<List<String>>(map.values());
    }
}