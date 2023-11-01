# 区块链包含区块
# 区块包含交易
# 所有的区块通过哈希散列函数链接在一起。
from Block import Block
import datetime

block_number = 10

blockchains = [Block.create_genesis_block()]

for i in range(1, block_number):
    blockchains.append(Block(blockchains[i-1].hash, "transaction_content", datetime.datetime.now()))
    print("区块{}已经被创建, 哈希是{}".format(i, blockchains[i].hash))
