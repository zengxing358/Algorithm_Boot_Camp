class Solution {
    public String longestPalindrome(String s) {
        int L=s.length();
        int p=(int)1e9+7;
        long[] pre=new long[L+1];
        long[] last=new long[L+1];
        long[] p131=new long[L+1];
        p131[0]=1;
        for(int i=0;i<L;i++){
            pre[i+1]=(pre[i]*131+(s.charAt(i)-'a'+1))%p;
            p131[i+1]=p131[i]*131%p;
        }
        for(int i=L-1;i>=0;i--){
            last[i]=(last[i+1]*131+(s.charAt(i)-'a'+1))%p;
        }
        for(int l=L;l>=1;l--){
            for(int left=0;left<=L-l;left++){
                int right=left+l-1;
                if(((pre[right+1]-pre[left]*p131[l])%p+p)%p==((last[left]-last[right+1]*p131[l])%p+p)%p){
                    return s.substring(left,right+1);
                }
            }
        }
        return s.substring(0,1);
    }
}