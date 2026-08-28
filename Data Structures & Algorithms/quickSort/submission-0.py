# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(0, len(pairs)-1, pairs)
        return pairs

    def quickSortHelper(self, s, e, pairs):
        if e-s+1 <= 1:
            return 
        left = s
        pt = 0
        piv = pairs[e]
        for i in range(s, e):
            if pairs[i].key < piv.key:
                tmp = pairs[i]
                pairs[i] = pairs[left]
                pairs[left] = tmp
                left+=1
        pairs[e] = pairs[left]
        pairs[left] = piv
        
        self.quickSortHelper(s, left-1, pairs)
        self.quickSortHelper(left+1, e, pairs)




