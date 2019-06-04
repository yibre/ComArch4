import sys
import math

read_access_count = 0
write_access_count = 0
total_access_count = 0
read_miss_count = 0
write_miss_count = 0
clean_eviction_count = 0
dirty_eviction_count = 0

# 여기는 건드릴 일 없음! 더이상 이 class를 호출할 일도, 함수를 쓸 일도 없음!
class CacheSet:
    def __init__(self, associativity):
        block = {"dirty": False, "tag": None} # 한 cache block
        self.set = []
        for i in range(associativity):
            self.set.append(block)

class Cache:
    def __init__(self, associativity, blockSize, capacity):
        self.associativity = associativity
        self.Cache = []
        self.blockOffset = math.log2(blockSize) # offset = log_2(blockSize)
        self.indexLength = capacity / blockSize / associativity * 1024
        # capacity(KB) / blockSize(B) / associativity =  index 의 길이
        # index 가 128까지 있으면 인덱스비트 7개 사용
        self.IndexBitLength = math.log2(self.indexLength)
        for i in range(self.indexLength):
            self.Cache.append(CacheSet(associativity))

    def access(self, address):
        for i in range(self.associativity):
            if self.Cache[self.findIndexBit(address)][i]['tag'] == self.findTagBit(address):
                temp = self.Cache[self.findIndexBit(address)][i]
                del self.Cache[self.findIndexBit(address)][i]
                self.Cache[self.findIndexBit(address)].append(temp)
                # 해당 원소가 있으면 list[index]의 해당 블록을 삭제하고 가장 뒤로 보냄 (for eviction)
                return True
        # 해당 원소가 없으면 false
        return False

    def cacheSetFull(self, address):
        for i in range(self.associativity):
            if not self.Cache[self.findIndexBit(address)][i]['tag']:
                return False
            # Cache set 안에 하나라도 빈 cache block 이 있으면 false 를 반환, set 이 전부 차 있으면 True 를 반환
        return True

    def add(self, address):
        global dirty_eviction_count, clean_eviction_count
        if self.cacheSetFull(address):
            if self.Cache[self.findIndexBit(address)][0]["dirty"]:
                dirty_eviction_count += 1
            del self.Cache[self.findIndexBit(address)][0]
            # 가장 첫번째 원소 삭제 -> LRU 구현
        # 가장 마지막에 원소 추가하기
        self.Cache[self.findIndexBit(address)].append({"dirty": False, "tag": self.findTagBit(address)})

    def read(self, address):
        global read_access_count, total_access_count, read_miss_count
        read_access_count += 1
        total_access_count += 1
        if not self.access(address): # read miss 발생
            read_miss_count += 1
        pass

    def write(self, address):
        global write_access_count, total_access_count, write_miss_count
        write_access_count += 1
        total_access_count += 1
        if self.access(address): # hit
            self.Cache[self.findIndexBit(address)][-1]['dirty'] = True
        else: # miss
            self.Cache[self.]


    def findTagBit(self, address): # return; int value
        TagBit = int(bin(address)[:-(self.blockOffset+self.IndexBitLength)], 2)
        return TagBit

    def findIndexBit(self, address): # return: int Index value
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