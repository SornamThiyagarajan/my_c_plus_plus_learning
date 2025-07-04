class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
         # Step 1: Build the length array
            lengths = [1]  # word starts as "a"
            for op in operations:
                lengths.append(lengths[-1] * 2)

            shift = 0  # count how many times we need to shift the final character

            # Step 2: Work backwards through the operations
            for i in range(len(operations)-1, -1, -1):
                prev_len = lengths[i]

                if k > prev_len:
                    k -= prev_len
                    if operations[i] == 1:
                        shift += 1  # we'll need to shift the character later
                else:
                    # k stays the same, but if op == 1, we did NOT shift for this half
                    continue

            # Step 3: Apply the shift on 'a'
            result_char = chr((ord('a') - ord('a') + shift) % 26 + ord('a'))
            return result_char