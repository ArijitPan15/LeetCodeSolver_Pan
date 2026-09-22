class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        prev = [0] * k

        for num in nums:
            curr = [0] * k

            # Subarray containing only num
            curr[num % k] += 1

            # Extend all previous subarrays
            for r in range(k):
                if prev[r] > 0:
                    new_r = (r * num) % k
                    curr[new_r] += prev[r]

            # Add subarrays ending at this position
            for r in range(k):
                ans[r] += curr[r]

            prev = curr

        return ans #for final changes
