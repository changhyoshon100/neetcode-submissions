class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        words = set(wordList)
        queue.append([beginWord, 1])
        visit = set()
        while queue:
            word, length = queue.popleft()
            if word in visit:
                continue
            visit.add(word)
            if word == endWord:
                return length
            
            # print(word)
            for i in range(len(word)):
                for c in "qwertyuiopasdfghjklzxcvbnm":
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in words:
                        queue.append((newWord, length + 1))
        
        return 0