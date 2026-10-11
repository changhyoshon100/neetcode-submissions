class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        minH = []
        minH.append((1, beginWord))
        heapq.heapify(minH)
        words = set(wordList)
        visited = set()
        while minH:
            length, word = heapq.heappop(minH)
            if word == endWord:
                return length
            if word in visited:
                continue
            visited.add(word)
            for i in range(len(word)):
                for ch in 'qwertyuiopasdfghjklzxcvbnm':
                    new_word = word[:i] + ch + word[i+1:]
                    
                    if new_word in words:
                        heapq.heappush(minH, (length + 1, new_word))
        return 0

