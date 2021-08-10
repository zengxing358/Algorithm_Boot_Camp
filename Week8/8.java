class Solution {
    public int myAtoi(String s) {
        if(s.length()==0){
            return 0;
        }
        int index=0;
        int pre=0;
        int sign=1;
        while (index<s.length() && s.charAt(index)==' '){
            index++;
        }
        if (index<s.length()&&(s.charAt(index)=='-'||s.charAt(index)=='+')){
            if (s.charAt(index)=='-'){
                sign=-1;
            }
            index++;
        }
        while (index<s.length()){
            int cur=s.charAt(index)-'0';
            if(cur<0||cur>9){
                break;
            }
            if (Integer.MAX_VALUE / 10 < pre || Integer.MAX_VALUE / 10 == pre && Integer.MAX_VALUE % 10 < cur)
            return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            pre=pre*10+cur;
            index++;
        }
        pre=pre*sign;
        return pre;
    }
}