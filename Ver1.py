import sys
import math

read_access_count = 0
write_access_count = 0
total_access_count = 0
read_miss_count = 0
write_miss_count = 0
clean_eviction_count = 0
dirty_eviction_count = 0

class CacheSet: # 여기는 건드릴 일 없음! 더이상 이 class를 호출할 일도, 함수를 쓸 일도 없음!
    def __init__(self, associativity):
        block = {"valid": False, "dirty": False, "tag": None} # 한 cache block
        self.set = []
        for i in range(associativity):
            self.set.append(block)

class Cache:
    def __init__(self, associativity, blockSize, capacity):
        self.Cache = []
        self.blockOffset = math.log2(blockSize) # offset = log_2(blockSize)
        self.indexLength = capacity / blockSize / associativity * 1024
        # capacity(KB) / blockSize(B) / associativity =  index 의 길이
        # index 가 128까지 있으면 인덱스비트 7개 사용
        self.IndexBitLength = math.log2(self.indexLength)
        for i in range(self.indexLength):
            self.Cache.append(CacheSet(associativity))

    def read(self, address):
        global read_access_count, total_access_count, read_miss_count
        read_access_count += 1
        total_access_count += 1

        pass

    def write(self, address):
        global write_access_count, total_access_count, write_miss_count
        write_access_count += 1
        total_access_count += 1

        pass

    def eviction(self, address): # LRU 구현 dirty eviction과 clean eviction 구현
        pass

    def findTagBit(self, address): # return; int 타입
        TagBit = int(bin(address)[:-(self.blockOffset+self.IndexBitLength)], 2)
        return TagBit

    def findIndexBit(self, address): # return: int 타입
        IndexBit = int('0b'+bin(address)[:(-self.blockOffset)][-(self.IndexBitLength):], 2)
        return IndexBit

    def file_read(self, file):
        for line in file:
            command, address_str = line.rstrip().split(' ')
            address = int(address_str, 16)
            if command == 'R':
                pass
            else:
                pass


if __name__ == "__main__":
    argv = sys.argv
    if ("-a" not in argv) or ("-c" not in argv) or ("-b" not in argv):
        print("ERROR!")
    else:
        capacity = argv[2]
        associativity = argv[4]
        blockSize = argv[-2]