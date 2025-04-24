class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        int n = nums.size();
        // 1. Total number of distinct values in nums
        unordered_set<int> distinct_set(nums.begin(), nums.end());
        int need = distinct_set.size();

        unordered_map<int, int> freq;
        int have = 0;
        long long ans = 0;
        int l = 0;

        // 2. Slide r from 0 to n-1
        for (int r = 0; r < n; ++r) {
            // Add nums[r]
            if (++freq[nums[r]] == 1) {
                // first time this value appears in window
                ++have;
            }

            // 3. While window [l..r] is complete, count and shrink from left
            while (have == need) {
                // All subarrays starting at l with end >= r are complete
                ans += (n - r);

                // Remove nums[l]
                if (--freq[nums[l]] == 0) {
                    // lost that distinct value
                    --have;
                }
                ++l;
            }
        }

        return ans;
    }
};