class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        res = [[p,s] for p,s in zip(position, speed)]
        # print(sorted(res)[::-1])
        for i,v in sorted(res)[::-1]:
            if time and time[-1] >= ((target - i) / v):
                continue
            time.append((target - i) / v)
        return len(time)

            