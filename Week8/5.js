var longestPalindrome = function(s) {
    var n=s.length
    if(n==0){
        return ""
    }
    anslen=1
    ansstart=0
    for(let center=1;center<n-1;center++){
        let l=center-1
        let r=center+1
        while((l>=0) && (r<n) && (s[l]==s[r])){
            l-=1
            r+=1
        }
        if (r-l-1>anslen){
            anslen=r-l-1
            ansstart=l+1
        }
    }
    for(let center=1;center<n;center++){
        let l=center-1
        let r=center
        while(l>=0 && r<n && s[l]==s[r]){
            l-=1
            r+=1
        }
        if (r-l-1>anslen){
            anslen=r-l-1
            ansstart=l+1
        }
    }
    return s.substring(ansstart,ansstart+anslen)
};