import datetime
import hashlib

class Block:
    def __init__(self, previous_block_hash, transaction, timestamp):
        self.previous_block_hash = previous_block_hash
        self.transaction = transaction
        self.timestamp = timestamp
        self.hash = self.get_hash()

    # 创建初始区块
    @staticmethod
    def create_genesis_block():
        return Block('0','0',datetime.datetime.now())

    def get_hash(self):
        header_bin = str(self.previous_block_hash) + str(self.transaction) + str(self.timestamp)
        out_hash = hashlib.sha256(header_bin.encode()).hexdigest()
        return out_hash
