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

# # Sliding Window 主要以右指针r为主，左指针只是位移标的，不参与真循环，这样就减少了一次循环嵌套。 Time O(n)  Space O(m)
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0
#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r-l+1)
#         return res

# Sliding Window (Optimal)   Time O(n) Space O(M)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} # 储存每个被遍历过的字母的最右边的位置序号
        l = 0
        res = 0
        for r in range(len(s)):
            # 利用map 的存储特性直接跳过重复，这是之前set不具备的，set可以去重，但不存储记录。所以只能加while 嵌套
            if s[r] in mp: # 如果当前遍历的字母出现了，说明之前有相同字母，那么，直接让左指针跳到这个之前的相同字母之后的一位继续，但是如果左指针当前位置已经比重复字母还靠后，就算了，说明是老早之前的重复
                l = max(mp[s[r]]+1, l)
            mp[s[r]] = r
            res = max(res, r-l+1)
        return res