class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 把 arr 里面的每一个数字 num 拿出来，先计算它和 x 的距离 abs(num-x)，然后按照这个距离从小到大排序；
        # 如果两个数字距离 x 一样，就按照数字本身 num 从小到大排序。
        arr.sort(key=lambda num: (abs(num-x), num))
        return sorted(arr[:k])