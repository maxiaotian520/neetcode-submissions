# # Brute Force  time O (n*k)   Space O(1)
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k %= n # k = k % n 让 k 变成 k 除以 n 后的余数。防止k数值过大套圈圈
#         while k: # 从最后一个nums搬数字到第一个
#             tmp = nums[n-1]
#             for i in range(n-1, 0, -1):
#                 nums[i] = nums[i-1] # 把数组中的所有元素整体向右移动一位，为 nums[0] 腾出位置。
#             nums[0] = tmp
#             k -= 1

# Extra Space  牺牲空间换时间  time O (n)   Space O(n) extra space  
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        tmp = [0] * n # 创建新的数组
        for i in range(n):
            # 向右旋转 k 位后，原来下标为 i 的元素，新下标是
            tmp[(i+k) % n] = nums[i] 
        nums[:] = tmp  # 表示把 tmp 中的所有内容复制到原来的 nums 数组中。不能用 nums = tmp, 这样只是改了指针
