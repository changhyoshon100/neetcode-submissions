class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            if target - numbers[i] in mp:
                return [mp[target - numbers[i]] + 1, i + 1]
            mp[numbers[i]] += i
