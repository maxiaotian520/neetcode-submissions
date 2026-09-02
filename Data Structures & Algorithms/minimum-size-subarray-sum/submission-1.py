# Brute force time O^2   Space 1
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = float("inf")
        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum += nums[j]
                if curSum >= target:
                    res = min(res, j-i+1)
                    break
        return 0 if res == float("inf") else res

# # Sliding window Time O(n)  Space O(1)
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         l, total = 0, 0
#         res = float("inf")
#         for r in range(len(nums)):
#             total += nums[r]
#             while total >= target:
#                 res = min(r-l+1, res)
#                 total -= nums[l]
#                 l += 1
#         return 0 if res == float("inf") else res

