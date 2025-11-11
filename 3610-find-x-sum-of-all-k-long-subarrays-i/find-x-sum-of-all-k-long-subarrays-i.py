class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
            n = len(nums)
            res = []
            window = nums[:k]
            counter = Counter(window)

            def compute_x_sum(counter):
                # Sort by freq descending, then value descending
                items = sorted(counter.items(), key=lambda item: (-item[1], -item[0]))
                top_x = items[:x]
                return sum(val * freq for val, freq in top_x)

            res.append(compute_x_sum(counter))

            for i in range(k, n):
                # remove outgoing element
                out_elem = nums[i - k]
                counter[out_elem] -= 1
                if counter[out_elem] == 0:
                    del counter[out_elem]
                # add incoming element
                in_elem = nums[i]
                counter[in_elem] += 1
                # compute x-sum for this window
                res.append(compute_x_sum(counter))

            return res