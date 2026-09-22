class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp = OrderedDict()

    def get(self, key: int) -> int:
        if not key in self.mp:
            return -1
        self.mp.move_to_end(key, last = True)
        return self.mp[key]

    def put(self, key: int, value: int) -> None:
        self.mp[key] = value
        self.mp.move_to_end(key, last = True)
        if len(self.mp) > self.cap:
            self.mp.popitem(last = False)
        
        
