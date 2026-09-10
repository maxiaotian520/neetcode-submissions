
# # Brute Force Time O(n) Space O(1)
# class MinStack:

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#     # 这个函数不是要返回什么值，而是把顶端的值删掉，不用返回任何值，不是top
#     def pop(self) -> None:
#         self.stack.pop()
        

#     def top(self) -> int:
#         return self.stack[-1]

#     # 创建个临时数组，一个个拿出来，挨个对比，找到最小的，然后再把临时队列里放回去 
#     def getMin(self) -> int:
#         tmp = []
#         mini = self.stack[-1]

#         while len(self.stack):
#             mini = min(mini, self.stack[-1])
#             tmp.append(self.stack.pop())
        
#         while len(tmp):
#             self.stack.append(tmp.pop())
#         return mini

# 
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # 为getMin 函数准备的

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 刚开始的数大，后面只有比它小的才能保存下俩，降序，min栈顶保存最小值
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

