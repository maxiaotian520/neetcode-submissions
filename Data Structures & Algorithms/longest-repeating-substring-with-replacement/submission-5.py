# # Brute force  Time O(n^2)   Space O(m)  但是运行超时
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         res = 0
#         for i in range(len(s)):
#             count, maxf = {}, 0
#             for j in range(i, len(s)):
#                 count[s[j]] = 1 + count.get(s[j], 0)
#                 maxf = max(maxf, count[s[j]])
#                 if (j-i+1) - maxf <= k:
#                     res = max(res, j-i+1)
#         return res

# Sliding Window  同样是双层嵌套，但是不是inner outer挨个遍历，而是把outer 部分用set 缩短，因此时间变成了O (M*N)
# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         res = 0
#         charSet = set(s)
#         for c in charSet:
#             count = l = 0
#             for r in range(len(s)):
#                 if s[r] == c:
#                     count += 1
                
#                 while (r-l+1) - count > k:
#                     if s[l] == c:
#                         count -= 1
#                     l += 1

#                 res = max(res, r-l+1)
#         return res

# 双侧window   O(n)  O(m)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r-l+1)-maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res




