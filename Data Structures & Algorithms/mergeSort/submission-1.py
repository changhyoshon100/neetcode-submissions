# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeHelper(0, len(pairs)-1, pairs)
    
    def mergeHelper(self, s, e, pairs):
        if e - s + 1 <= 1:
            return pairs
        m = (s + e) // 2  
        self.mergeHelper(s, m, pairs)
        self.mergeHelper(m+1, e, pairs)
        self.merge(s,m,e,pairs)
        return pairs

    def merge(self,s,m,e,pairs):
        L = pairs[s:m+1]
        R = pairs[m+1:e+1]
        i = 0
        j = 0
        k = s
        
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i+=1
                
            else:
                pairs[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            pairs[k] = L[i]
            k+=1
            i+=1
        while j < len(R):
            pairs[k] = R[j]
            k+=1
            j+=1
        



