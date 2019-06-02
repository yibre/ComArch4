import sys


class CacheSet:
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


if __name__ == "__main__":
    argv = sys.argv
    if ("-a" not in argv) or ("-c" not in argv) or ("-b" not in argv):
        print("ERROR!")
    else:
        capacity = argv[2]
        associativity = argv[4]
        blockSize = argv[-2]