class Solution {
public:
    //Sornam Thiyagarajan
    vector<int> runningSum(vector<int>& nums) {
        vector<int> result(nums.size(),0); //Create a new array to store the result array 
        result[0]= nums[0];
       for(int i = 1; i < nums.size(); ++i)
       {
        result[i]=result[i-1]+nums[i];  //calcaulation res = arr[0]+arr[curr]
       }
       for(int num:result)
       {
        cout<<num<<" ";
        //cout<< "Size:" <<nums.size() <<endl;
        //cout << "Capacity:" <<nums.capacity() <<endl;
       }  cout<<endl;

       return result;
    }
};