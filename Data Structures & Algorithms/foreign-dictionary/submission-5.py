class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = set()
        visiting = set()
        res = []

        def dfs(curr):
            if curr in visiting:
                return False
            if curr in visited:
                return True
            
            visiting.add(curr)
            for nei in adj[curr]:
                if not dfs(nei):
                    return False
            visiting.remove(curr)

            visited.add(curr)
            res.append(curr)
            return True

        for i in adj:
            if not dfs(i):
                return ""
        res.reverse()

        return "".join(res)


        


                