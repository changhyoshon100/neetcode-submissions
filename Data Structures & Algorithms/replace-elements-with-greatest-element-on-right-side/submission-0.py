class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = arr[len(arr) - 1]
        result = [-1]
        if len(arr) == 1:
            return result
        for i in range(len(arr) - 2, -1, -1):
            result = [greatest] + result
            if arr[i] > greatest:
                greatest = arr[i]
        return result


