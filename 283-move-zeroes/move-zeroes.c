void moveZeroes(int* nums, int numsSize) {
    int last_non_zero = 0 ; 

  // Move non-zero elements to the front 
    for (int i = 0; i < numsSize; i++)
    {
        if (nums[i] != 0)
        {
            nums[last_non_zero] = nums[i];
            last_non_zero += 1; 
        }
    }
        //Fill remaining positions with 0 
        for (int j = last_non_zero ; j < numsSize; j++)
        {
            nums[j] = 0 ; 
        }

           
    
}