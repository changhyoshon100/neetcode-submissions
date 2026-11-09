class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.map.move_to_end(key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        self.map[key] = value
        self.map.move_to_end(key)
        if len(self.map) > self.cap:
            self.map.popitem(last=False)

        
