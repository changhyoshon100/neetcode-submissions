class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque()
        queue.append([beginWord, 1])
        wordList = set(wordList)
        
        while queue:
            for i in range(len(queue)):
                word, length = queue.popleft()
                if word == endWord:
                    return length
                
                for i in range(len(word)):
                    for ch in "qwertyuioplkjhgfdsazxcvbnm":
                        new_word = word[:i] + ch + word[i+1:]
                        if new_word in wordList:
                            wordList.remove(new_word)
                            queue.append((new_word, length + 1))
        return 0
