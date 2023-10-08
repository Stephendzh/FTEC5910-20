# from pythonds.basic import Stack
# # 括号匹配问题
# def parchecker(symbolSting):
#     indice = 0
#     s = Stack()
#     while indice < len(symbolSting):
#         if symbolSting[indice] == '(':
#             s.push(symbolSting[indice])
#         elif symbolSting[indice] == ')':
#             if s.isEmpty():
#                 match = False
#                 return match
#             s.pop()
#         indice += 1
#     match = s.isEmpty()
#     return match
#
#
# print(parchecker('((()))'))
# print(parchecker('(()))())'))
# print(parchecker('((())'))
#
# # 多种括号的匹配问题
# def parchecker1(symbolString):
#     s = Stack()
#     balanced = True
#     index = 0
#     while index < len(symbolString) and balanced:
#         symbol = symbolString[index]
#         if symbol in '([{':
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 balanced = False
#             else:
#                 top = s.pop()
#                 if not matches(top, symbol):
#                     balanced = False
#         index += 1
#     if balanced and s.isEmpty():
#         return True
#     else:
#         return False
#
# def matches(open, close):
#     opens = '([{'
#     closers = ')]}'
#     return opens.index(open) == closers.index(close)
#
#
# print(parchecker1('{{()}}'))
# print(parchecker1('[{(}){'))


minutes = int(input('Input Minutes:'))
days = minutes // 1440
rest1 = minutes % 1440
hours = rest1 // 60
rest2 = rest1 % 60
print(f'{days} days {hours} hours {rest2} minutes')