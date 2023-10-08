def odd(n):
    return (n % 2 != 0)

def even(n):
    return (n % 2 == 0)

def pos(mylist, func):
    truelist = []
    for i in range(len(mylist)):
        if func(i):
            truelist.append(i)
    return truelist

# list1 = [i for i in range(10)]
# print(pos(list1, even))
# f = open("test.txt", 'w')
# f.write(' This is my first text file with python')
# f.close()
#
# f = open('test.txt', 'r')
# print(f.read())
# f.close()
# import os
# if os.path.exists('test.txt'):
#     os.remove('test.txt')
#     print('Successfully removed')
# else:
#     print('Not exists')

import pickle
# f = open('filename', 'rb')   # open file in binary mode

myDict = {'Orange': 1, 'Apple': 4, 'Melon': 7}
mylist =[1, 2, 3]
f = open('fruit.pkl', 'wb')
pickle.dump(myDict, f) # Data1 is a Dictionary
pickle.dump(mylist, f)
f.close()

f = open('fruit.pkl', 'rb')
newNum = pickle.load(f)
newDict = pickle.load(f)
print(newNum)
print(newDict)
f.close()