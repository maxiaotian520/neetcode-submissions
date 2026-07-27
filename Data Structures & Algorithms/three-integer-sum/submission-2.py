# # Brute Force O(n^3)
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = set()
#         nums.sort()
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         tmp = [nums[i], nums[j], nums[k]]
#                         res.add(tuple(tmp))
#         return [list(i) for i in res]

# Hash Map Time: O(n~2), Space O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums)-2):
            seen = set()
            for j in range(i+1, len(nums)):
                target = -nums[i] - nums[j]

                if target in seen:
                    triplet = tuple(sorted((nums[i], nums[j], target)))
                    res.add(triplet)
                seen.add(nums[j])
        
        return [list(tri) for tri in res]




















