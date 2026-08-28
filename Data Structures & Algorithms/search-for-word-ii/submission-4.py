class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0
    
    def addWord(self, word):
        cur = self
        cur.refs += 1
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
            cur.refs += 1
        cur.isWord = True
    
    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
                cur.refs -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visit, res = set(), set()
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()
        for word in words:
            root.addWord(word)
            

        def dfs(r,c,word,node):
            if (
                r not in range(ROWS)
                or c not in range(COLS)
                
                or board[r][c] not in node.children
                or node.children[board[r][c]].refs < 1
                or (r,c) in visit
            ):
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                root.removeWord(word)
                res.add(word)
            
            dfs(r + 1, c, word, node)
            dfs(r - 1, c, word, node)
            dfs(r, c + 1, word, node)
            dfs(r, c - 1, word, node)
            visit.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,"", root)
        return list(res)