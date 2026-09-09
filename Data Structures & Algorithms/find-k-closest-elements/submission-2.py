# #Sorting time O(nlogn + klogk) Space O(!)
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         # 把 arr 里面的每一个数字 num 拿出来，先计算它和 x 的距离 abs(num-x)，然后按照这个距离从小到大排序；
#         # 如果两个数字距离 x 一样，就按照数字本身 num 从小到大排序。
#         arr.sort(key=lambda num: (abs(num-x), num))
#         return sorted(arr[:k])

# # Linear Scan + two pointers    找到距离最小的点，以它为中心做右指针向外扩散 注意，这里arr 是sorted, 所以可以用这个方法
# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         # step 1, 找到全局距离x最近点idx
#         n = len(arr)
#         idx = 0
#         for i in range(1, n):
#             if abs(x - arr[idx]) > abs(x-arr[i]):
#                 idx = i
#         res = [arr[idx]]
#         # step 2  以这个点为中心，左右指针l,r 分别阔
#         l, r = idx - 1, idx + 1
#         # ste
#         while len(res) < k:
#             if l >= 0 and r < n:
#                 if abs(x - arr[l]) <= abs(x - arr[r]):
#                     res.append(arr[l])
#                     l -= 1
#                 else:
#                     res.append(arr[r])
#                     r += 1
#             elif l >= 0:
#                 res.append(arr[l])
#                 l -= 1
#             elif r < n:
#                 res.append(arr[r])
#                 r += 1
#         return sorted(res)
# two pointers Time(n-k)  Space O(k) 注意，这里arr 是sorted, 所以可以用这个方法
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r =0, len(arr) - 1
        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        return arr[l: r + 1]
