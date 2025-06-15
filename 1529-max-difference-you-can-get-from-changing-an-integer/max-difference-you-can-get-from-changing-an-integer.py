class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # Maximize: replace first digit that is not '9' with '9'
        for d in s:
            if d != '9':
                max_num = int(s.replace(d, '9'))
                break
        else:
            max_num = num  # all digits are already 9

        # Minimize:
        if s[0] != '1':
            min_num = int(s.replace(s[0], '1'))
        else:
            for d in s[1:]:
                if d != '0' and d != '1':
                    min_num = int(s.replace(d, '0'))
                    break
            else:
                min_num = num  # all digits are 0 or 1

        return max_num - min_num