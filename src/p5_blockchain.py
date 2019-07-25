import hashlib
from datetime import datetime


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.start = None

    def append(self, value):
        new_node = Node(value)
        if self.start is None:
            self.start = new_node
            return
        last_node = self.start
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node


class Block:
    def __init__(self, data, previous_hash, timestamp=datetime.now().timestamp()):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = (self.data + str(self.timestamp) + self.previous_hash).encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_formatted_timestamp(self):
        return datetime.utcfromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self):
        return "{{Date: {}, Data: \"{}\", hash: {}, previous_hash: {}}}"\
            .format(self.get_formatted_timestamp(), self.data, self.hash, self.previous_hash)


class BlockChain:
    def __init__(self):
        self.blocks = LinkedList()
        self.last_block = None

    def get_last_block(self):
        return self.last_block

    def add_block(self, block: Block):
        if self.last_block is None:
            self._append(block)
            return True
        if self.last_block.hash == block.previous_hash:
            self._append(block)
            return True
        return False

    def _append(self, block):
        self.blocks.append(block)
        self.last_block = block

    def __str__(self):
        return_str = '['
        node = self.blocks.start
        while node:
            return_str += '\n\t' + str(node.get_value())
            node = node.next
            if node:
                return_str += ','
            else:
                return_str += '\n'
            #return_str += '\n'
        return_str += ']'
        return return_str


blockchain = BlockChain()

block_0 = Block('This is the first block!', '0')
print(block_0)
print('Block inserted: ' + str(blockchain.add_block(block_0)))  # Should return True
print()

block_1 = Block('This is the second block!', block_0.hash)
print(block_1)
print('Block inserted: ' + str(blockchain.add_block(block_1)))  # Should return True
print()

block_2 = Block('This is the third block!', block_1.hash)
print(block_2)
print('Block inserted: ' + str(blockchain.add_block(block_2)))  # Should return True
print()

invalid_block = Block('This is invalid block!', '123456789')
print(invalid_block)
print('Block inserted: ' + str(blockchain.add_block(invalid_block)))  # Should return False
print()

print('Blockchain: ' + str(blockchain))

empty_blockchain = BlockChain()
print()
print('Empty Blockchain: ' + str(empty_blockchain))  # Empty list as the blockchain is empty
