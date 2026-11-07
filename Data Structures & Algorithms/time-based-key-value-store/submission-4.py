class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key] = []
        self.mp[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        name = self.mp[key]
        left = 0
        right = len(name) - 1
        res = ""
        while left <= right:
            mid = (left + right) // 2
            if name[mid][0] <= timestamp:
                res = name[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res






        
