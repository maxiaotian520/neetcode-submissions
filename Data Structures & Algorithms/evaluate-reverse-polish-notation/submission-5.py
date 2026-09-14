#逆波兰表达式（Reverse Polish Notation, RPN） 的写法。名字听起来很吓人，其实规则很简单：运算符写在数字后面，而且不需要括号
# tokens = ["1", "2", "+", "3", "*", "4", "-"]
# 1 2 + = 3, 3 3 * = 9, 9 4 -= 5, 所以答案是5
# Brute Force Time O（N^2), Space O(n)
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         # 如果只看“遍历 tokens”这件事，确实一个 for 就够；但这份代码里的 for 每次只打算处理一个运算符，所以外面必须再套一个 while。但是for 最底下有个Break, 也就是说，碰到运算符号，就要开始计算前面的，然后终结运算符。如果没有外层while, 就只计算一次就终结了。
#         while len(tokens) > 1:
#             for i in range(len(tokens)):
#                 if tokens[i] in "+-*/":
#                     a = int(tokens[i-2])
#                     b = int(tokens[i-1])
#                     if tokens[i] == '+':
#                         result = a + b
#                     elif tokens[i] == '-':
#                         result = a - b
#                     elif tokens[i] == '*':
#                         result = a * b
#                     elif tokens[i] == '/':
#                         result = int(a / b)
#                     tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
#                     break
#         return int(tokens[0])

# Stack Time O(n) Space (N)
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         for c in tokens:
#             if c == "+":
#                 stack.append(stack.pop() + stack.pop())
#             elif c == "-":
#                 # 这里注意，因为减法和除法前后顺序很重要，所以必须先pop 出数字表明谁先谁后，然后再运算，而+和*不用
#                 # 比如[2,10], 这里如果直接用stack.append(stack.pop() - stack.pop())，就是2-10, 必须反过来
#                 a, b = stack.pop(), stack.pop()
#                 stack.append(b - a)
#             elif c == "*":
#                 stack.append(stack.pop() * stack.pop())
#             elif c == "/":
#                 a,b = stack.pop(), stack.pop()
#                 stack.append(int(b/a))
#             else:
#                 stack.append(int(c))
#         return stack[0]

# Recursion  Time O(n)  Space O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
# 详解：
# dfs() 的任务是：从 tokens 的最后面，算出一个完整表达式的值
# tokens = ["2", "1", "+", "3", "*"]  它表示：(2 + 1) * 3
# 如果画成一棵树，就是：
#           *
#         /   \
#        +     3
#       / \
#      2   1
# 逆波兰表达式其实就是按照：左边 → 右边 → 运算符来写，所以：2 1 + 3 * 
        def dfs():
            token = tokens.pop()
            # ["2", "1", "+", "3", "*"] pop() 默认拿最后一个。第一次拿出来 *，所以下面的if语句先跳过
            if token not in "+-*/":
                return int(token)
            # 然后遍历之前的叶子节点，左 & 右
            right = dfs()
            left = dfs()

            if token == "+":
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)
        return dfs()

