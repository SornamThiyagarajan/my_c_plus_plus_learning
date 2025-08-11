int divide(int dividend, int divisor) {
    // Handle the case where dividend is equal to divisor 
    if (dividend == divisor) return 1;

    unsigned int ans = 0;
    int sign = 1; 

    //Determine the sign of the result 
    if ((dividend < 0 && divisor > 0) || (dividend > 0 && divisor < 0 ))
        sign = -1; 
    
    //Convert both dividend and divisor to positive integers 
    //unsigned int n = abs(dividend) , d = abs(divisor);
    unsigned int n = (dividend < 0) ? (unsigned int)(-(long long)dividend) : (unsigned int)dividend;
    unsigned int d = (divisor < 0) ? (unsigned int)(-(long long)divisor) : (unsigned int)divisor;


    //Perform the actual divison 
    while (n >=d){
        int count = 0; 
        while (n > (d << (count+1))){
            count++;
        }
        n -= d << count; 
        ans += 1 << count; 
    }

    //Handle overflow case 
    if (ans == (1U << 31) && sign == 1) return INT_MAX; 


    return sign * ans; 
}