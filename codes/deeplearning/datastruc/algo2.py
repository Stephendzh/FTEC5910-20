# 继承与逻辑门
# 每个逻辑门都有一个用于识别的标签，以及一个输出，此外还需要一些方法以便用户获取逻辑门的标签
class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.PerformGateLogic()
        return self.output
    # 暂时不用实现performgatelogic函数


class BinaryGate(LogicGate):
    """LogicGate的一个子类，并且有两个输入"""

    def __init__(self, n):
        # 首先使用super函数调用父类的构造方法
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input('Enter Pin A input for gate' + self.getLabel() + '--->'))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input('Enter Pin B input for gate' + self.getLabel() + '--->'))
        else:
            return self.pinB.getFrom().getOutput()


class UnaryGate(LogicGate):
    """LogicGate的一个子类， 但只有一个输入"""

    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input('Enter Pin A input for gate' + self.getLabel() + '--->'))
        else:
            return self.pin.getFrom().getOutput()


# 有了不同输入个数的逻辑门通用类之后， 就可以有独特行为的逻辑门构建类。例如：由于 “与门” 有两个输入
# 因此AndGate 是 BinaryGate 的子类
# 构造方法的第一行调用父类（BinaryGate）的构造方法，该构造方法又会调用它的父类LogicGate的构造方法
# 注意 由于继承了两个输入， 一个输出和逻辑门标签，因此AndGate并没有添加新的数据
class AndGate(BinaryGate):
    """在这里实现PerformGateLogic"""

    def __init__(self, n):
        super().__init__(n)

    def PerformGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

    def SetNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError('No Empty Pins')


class OrGate(BinaryGate):

    def __init__(self, n):
        super().__init__(n)

    def PerformGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 0
        else:
            return 1

    def SetNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError('No Empty Pins')


class NotGate(UnaryGate):

    def __init__(self, n):
        super().__init__(n)

    def PerformGateLogic(self):
        i = self.getPin()
        if i == 1:
            return 0
        else:
            return 1

    def SetNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError('No Empty Pins')


# 有了逻辑门之后可以开始构建电路，为此要吧逻辑门连接在一起
# Connector类并不在逻辑门的继承层次结构当中

class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        # 首先应该包含fromgate和togate两个逻辑门实例
        # 数据从一个逻辑门的输出流向另一个逻辑门的输入
        # 对SetNextPin的调用对于实现连接非常重要，需要将这个方法添加到逻辑门类中
        # 使得每一个togate能够选择适当的输入
        tgate.SetNextPin(source=self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


g1 = AndGate('g1')
g2 = AndGate('g2')
g3 = OrGate('g3')
g4 = NotGate('g4')
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)
print(g4.getOutput())
