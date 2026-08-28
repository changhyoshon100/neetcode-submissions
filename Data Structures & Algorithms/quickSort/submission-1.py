# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.q_sort(0, len(pairs) - 1, pairs)
        return pairs

    def q_sort(self, s, e, pairs):
        if e - s + 1 <= 1:
            return 

        pivot = pairs[e]
        ptr = s
        left = s
        while ptr < e:
            if pairs[ptr].key < pivot.key:
                pairs[ptr], pairs[left] = pairs[left], pairs[ptr]
                left += 1
            ptr += 1
    
        pairs[e] = pairs[left]
        pairs[left] = pivot
        
        self.q_sort(s, left - 1, pairs)
        self.q_sort(left + 1, e, pairs)
