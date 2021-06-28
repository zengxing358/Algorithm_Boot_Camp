class Solution {
    public double myPow(double x, long n) {
    if(n<0) return 1/myPow(x,-n);
    if(n==0) return 1;
    if(n%2==0) return Math.pow(myPow(x,n/2),2);
    return x*Math.pow(myPow(x,n/2),2);

    }
}