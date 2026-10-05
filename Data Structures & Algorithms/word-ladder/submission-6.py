class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append((beginWord, 0))
        words = set(wordList)
        visited = set()
        while queue:
            word, length = queue.popleft()
            print(word)
            if word == endWord:
                return length + 1
            if word in visited:
                continue
            visited.add(word)
            for i in range(len(word)):
                for c in 'qwertyuioplkjhgfdsazxcvbnm':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in words:
                        queue.append((new_word, length + 1))
        return 0
                    
            
            