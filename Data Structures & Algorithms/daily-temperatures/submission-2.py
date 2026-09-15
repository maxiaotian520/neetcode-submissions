# 对每一天，找它后面第一次出现“更高温度”的那一天，然后计算要等几天
# # Brute Force Time O(n^2), Space O(n)
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         n = len(temperatures)
#         res = []
#         for i in range(n):
#             count = 1
#             j = i + 1
#             while j < n:
#                 if temperatures[j] > temperatures[i]:
#                     break
#                 j += 1
#                 count += 1
#             count = 0 if j == n else count
#             res.append(count)
#         return res

# # Stack  Time O(n) Space O(n)
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         res = [0] * len(temperatures)
#         stack = []
#         for i, t in enumerate(temperatures):
#             while stack and t > stack[-1][0]: # [-1] 栈顶 [0] 提取(a，b)的a
#                 stackT, stackInd = stack.pop()
#                 res[stackInd] = i - stackInd
#             stack.append((t, i))
#         return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n-2, -1, -1):
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]            
            if j < n:
                res[i] = j - i
        return res









