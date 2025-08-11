char* addBinary(char* a, char* b) {
    // Store length of a and b 
    int lenA = strlen(a);
    int lenB = strlen(b);
    
    //Initialize two indices of i and j pointing to the last charcter of string a and b and initalize carry as 0 
    int i = lenA - 1;
    int j = lenB - 1;
    int carry = 0;

    int maxLen = (lenA > lenB ? lenA : lenB) + 2;
    char* result = (char*)malloc(maxLen);
    int k = 0;
    while (i >= 0 || j >= 0 || carry) {
            int total = carry;

            if (i >= 0) {
                total += a[i] - '0';  // convert char to int
                i--;
            }
            if (j >= 0) {
                total += b[j] - '0';  // convert char to int
                j--;
            }

            result[k++] = (total % 2) + '0';  // store result bit as char
            carry = total / 2;                 // update carry
        }

        // result is currently reversed, reverse it back
        result[k] = '\0';

        // Reverse the string in place
        for (int left = 0, right = k - 1; left < right; left++, right--) {
            char temp = result[left];
            result[left] = result[right];
            result[right] = temp;
        }

        return result;  // caller must free the returned string
}