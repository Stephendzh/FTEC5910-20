class Stack:
    def __init__(self):
        self.items = []

    def is_Empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

# 匹配括号问题
# 从左到右处理括号，使用栈是合理的，由一个空栈开始，如果遇到左括号，就通过push操作将其加入栈
# 如果遇到右括号就调用pop操作，只要栈中的所有左括号都能遇到与之对应的右括号，整个括号串匹配
# 处理完之后，整个栈应该是空的
