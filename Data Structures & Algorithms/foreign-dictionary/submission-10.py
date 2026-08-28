class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        for word in words:
            for c in word:
                adj[c]

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2):
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = set()
        cycle = set()
        res = []

        def dfs(curr):
            if curr in cycle:
                return False
            if curr in visit:
                return True
            
            cycle.add(curr)
            for nei in adj[curr]:
                if not dfs(nei):
                    return False
            cycle.remove(curr)
            visit.add(curr)
            res.append(curr)
            return True
        

        for c in adj:
            if not dfs(c):
                return ""
        res.reverse()
        return ''.join(res)
                    
