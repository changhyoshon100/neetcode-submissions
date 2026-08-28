class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def add(self, word):
        cur = self
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = TrieNode()
            cur = cur.children[word[i]]
        cur.isWord = True
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        ans = set()
        for w in words:
            self.root.add(w)

        def dfs(r,c, node, res):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r,c))
            res += board[r][c]
            node = node.children[board[r][c]]
            if node.isWord:
                ans.add(res)
            dfs(r+1,c,node,res)
            dfs(r-1,c,node,res)
            dfs(r,c+1,node,res)
            dfs(r,c-1,node,res)
            visit.remove((r,c))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, self.root, "")
        return list(ans)



        