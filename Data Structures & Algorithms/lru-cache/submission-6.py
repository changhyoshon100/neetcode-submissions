class LRUCache:

    def __init__(self, capacity: int):
        self.mp = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.mp:
            return -1
        self.mp.move_to_end(key, last=True)
        return self.mp[key]

    def put(self, key: int, value: int) -> None:
        self.mp[key] = value
        self.mp.move_to_end(key,last=True)
        
        if self.capacity < len(self.mp):
            self.mp.popitem(last=False)
        
            


