class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> magazineCount; 

        // Count the frequency of each character in the magazine
        for (char ch : magazine) {
            magazineCount[ch]++;
        }
        // Check if we can construct the ransomNote
        for (char ch : ransomNote) {
            if (magazineCount[ch] > 0) {
                magazineCount[ch]--;
            } else {
                return false;  // If a character is not available, return false
            }
        }        
    return true;  // If we can form the ransom note, return true
    }
    
};