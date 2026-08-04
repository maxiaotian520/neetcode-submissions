# Brute Force  time O (n*k)   Space O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n # k = k % n 让 k 变成 k 除以 n 后的余数。防止k数值过大套圈圈
        while k: # 从最后一个nums搬数字到第一个
            tmp = nums[n-1]
            for i in range(n-1, 0, -1):
                nums[i] = nums[i-1] # 把数组中的所有元素整体向右移动一位，为 nums[0] 腾出位置。
            nums[0] = tmp
            k -= 1
