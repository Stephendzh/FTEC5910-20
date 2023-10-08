# 面向对象编程：定义类
# 创建分数类 Fraction
class Fraction:
    # 所有的类都应该有构造方法，构造方法定义了数据对象的创建方式 python中，构造方法总是为__init__
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
    # 形式参数列表包括三项，self是一个总是指向对象本身的特殊参数，必须是第一个形式参数
    def show(self):
        print(self.num, "/", self.den)
    # 所有类都提供了一套标准方法，但是可能没有正常工作，其中之一就是
    #对象转换为字符串方法 __str__
    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        newnum = self.num * other.den + \
                    self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n

myfrc = Fraction(3, 5)
print(myfrc.__str__())
print(myfrc)
