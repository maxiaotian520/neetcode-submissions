# # Bruth Force n^3log (嵌套循环 n^2, 然后一个子串排序 substr = sorted(substr)) 为nlogn, 相乘后就是;   n Space 
# class Solution:
# def checkInclusion(self, s1: str, s2: str) -> bool:
#     s1 = sorted(s1)

#     for i in range(len(s2)):
#         for j in range(i, len(s2)):
#             substr = s2[i:j+1]
#             substr = sorted(substr)
#             if substr == s1:
#                 return True
#     return False

#
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in s1:
            count1[c] = 1 + count1.get(c, 0)
        
        need = len(count1)
        for i in range(len(s2)):
            count2, cur = {}, 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j], 0)
                if count1.get(s2[j], 0) < count2[s2[j]]: # 子字符串数量都不够，根本不用再看了，不合适，直接终止
                    break
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False
                