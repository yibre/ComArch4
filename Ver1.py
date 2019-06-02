import sys

read_access_count = 0
write_access_count = 0
total_access_count = 0
read_miss_count = 0
write_miss_count = 0
clean_eviction_count = 0
dirty_eviction_count = 0

class CacheSet: # 여기는 건드릴 일 없음! 더이상 이 class를 호출할 일도, 함수를 쓸 일도 없음!
    def __init__(self, associativity):
        block = {"valid": False, "dirty": False, "tag": None}
        self.set = []
        for i in range(associativity):
            self.set.append(block)

class Cache:
    def __init__(self, associativity, index):
        self.Cache = []
        for i in range(index):
            self.Cache.append(CacheSet(associativity))

    def find(self, index, tag):
        self.Cache[index]
        pass

    def add(self, tag):
        pass

    def read(self, address):
        pass

    def write(self, address):
        pass

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