int hammingWeight(int n) {
    
    int remainder = 0 ;
    int setbit_cnt = 0;
    if (n == 0) {
        return setbit_cnt;
    }
        
    
    while (n > 0) {
        remainder = n % 2 ;
        if (remainder == 1)
           {
           setbit_cnt += 1 ;
           } 
        n = n / 2 ;
    } 
        
    

    return setbit_cnt ;

        
}