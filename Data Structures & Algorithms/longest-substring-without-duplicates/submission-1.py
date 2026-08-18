# # Brute Force  Time: O(n*m), Space O(m)   两个左右指针i, j，i固定，j 向右遍历，遇到重复就终止，记录下长度，然后i 右移一位，再来  (需要两个指针嵌套for loop)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         res = 0
#         for i in range(len(s)):
#             charSet = set()
#             for j in range(i, len(s)):
#                 if s[j] in charSet:
#                     break
#                 charSet.add(s[j])
#             res = max(res, len(charSet))
#         return res

# Slide Window 主要以右指针r为主，左指针只是位移标的，不参与真循环，这样就减少了一次循环嵌套。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
        return res