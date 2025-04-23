class Solution {

int digitsum(int num){
    int sum = 0;
    while(num > 0){
        sum += num % 10 ; 
        num/=10;
    }
    return sum;
}

public:
    int countLargestGroup(int n) {
        unordered_map<int, vector<int>> groups;
        for (int i = 1;i<=n; i++){
            int sum = digitsum(i);
            groups[sum].push_back(i) ;           
        }

        vector<int>sizes;
        for (const auto&pair:groups){
            sizes.push_back(pair.second.size());
        }

        if (sizes.empty()) return 0;
        int max_size = *max_element(sizes.begin(), sizes.end());

        int count = 0; 
        for (int size : sizes){
            if (size == max_size){
                count++;
            }
        }
        return count ;
    }
};