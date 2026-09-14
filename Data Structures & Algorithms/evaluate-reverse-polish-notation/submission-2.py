#逆波兰表达式（Reverse Polish Notation, RPN） 的写法。名字听起来很吓人，其实规则很简单：运算符写在数字后面，而且不需要括号
# tokens = ["1", "2", "+", "3", "*", "4", "-"]
# 1 2 + = 3, 3 3 * = 9, 9 4 -= 5, 所以答案是5
# Brute Force Time O（N^2), Space O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 如果只看“遍历 tokens”这件事，确实一个 for 就够；但这份代码里的 for 每次只打算处理一个运算符，所以外面必须再套一个 while。但是for 最底下有个Break, 也就是说，碰到运算符号，就要开始计算前面的，然后终结运算符。如果没有外层while, 就只计算一次就终结了。
        while len(tokens) > 1:
            for i in range(len(tokens)):
                if tokens[i] in "+-*/":
                    a = int(tokens[i-2])
                    b = int(tokens[i-1])
                    if tokens[i] == '+':
                        result = a + b
                    elif tokens[i] == '-':
                        result = a - b
                    elif tokens[i] == '*':
                        result = a * b
                    elif tokens[i] == '/':
                        result = int(a / b)
                    tokens = tokens[:i-2] + [str(result)] + tokens[i+1:]
                    break
        return int(tokens[0])

# Stack Time O(n) Space (N)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]