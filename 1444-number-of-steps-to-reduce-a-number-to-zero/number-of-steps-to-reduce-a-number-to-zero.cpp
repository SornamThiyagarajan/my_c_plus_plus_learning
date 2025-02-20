class Solution {
public:
    int numberOfSteps(int num) {
        int stepcnt =0;
        while(num>0)
        {
            if (num%2==0) //step1: need to divide by 2 
            {
                num/=2;
            }
            else
            {
                num--; //subtract by 1 if it is odd 
            }
        stepcnt++;  //return the stepcount as result 
        }
        return stepcnt;
    }
};

//Time Complexity O(logn)
//Space Complexity O(1)