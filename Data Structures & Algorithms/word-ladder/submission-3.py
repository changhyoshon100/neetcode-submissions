class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        length = 1
        queue = deque([(beginWord, length)])
        words = set(wordList)
        
        while queue:
            word, length = queue.popleft()
            if word == endWord:

                return length
            
            for i in range(len(word)):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in words:
                        words.remove(new_word)
                        queue.append([new_word, length + 1])
        return 0
