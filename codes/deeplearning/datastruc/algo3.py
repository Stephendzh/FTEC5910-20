# 异序词检测问题：如果一个字符串只是重拍了另一个字符串的字符，那么这个字符串就是另一个的异序词
# 如： heart和earth   python和Typhon
# 首先假设要检查的两个字符串的长度相同，并且都是由26个英文字母的小写形式组成的
import time
start_time = time.time()

def Solution(s1, s2):
    set1 = set(list(s1))
    set2 = set(list(s2))
    print(set1 == set2)

Solution('heart', 'earth')
end_time = time.time()
elapsed_time = end_time - start_time
print(f"程序运行时间：{elapsed_time:.8f} 秒")

start_time = time.time()
# 排序法
def Solution1(s1, s2):
    """尽管s1 和 s2是不同的字符串，但是只要由相同的字符构成，它们就是异序词
        按照字母表给字符排序，异序词得到的结果将是同一个字符串
        在python中，可以先将字符串转化为列表然后使用sort方法
    """
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    position = 0
    matches = True
    while position < len(s1) and matches:
        if alist1[position] == alist2[position]:
            position += 1
        else: matches = False
    return matches


