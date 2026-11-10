class TrieNode:
    def __init__(self, currLetter):
        self.letter = currLetter
        self.children = {}

    def addWord(self, word, i):
        word += '0'
        currNode = self
        for ch in word:
            if(ch in currNode.children):
                currNode = currNode.children[ch]
            else:
                currNode.children[ch] = TrieNode(ch)
                currNode = currNode.children[ch]

    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode("")

        DIRECTIONS = [
            [-1, 0],
        [0, -1], [0,0],    [0, 1],
            [1, 0]
        ]

        for i in range(len(words)):
           root.addWord(words[i], i)
        
        
        def inBounds(row, col):
            if(row >= 0 and row < len(board) and col >= 0 and col < len(board[0])):
                return True
            return False

        foundWords = set()

        
        
        def investigateCell(r, c, node, currStr):
            letter = board[r][c]
            board[r][c] = '1'
            if('0' in node.children):
                foundWords.add(currStr)
            if(node and (letter in node.children)):
                for addR, addC in DIRECTIONS:
                    newR = r + addR
                    newC = c + addC
                    if(inBounds(newR, newC)):
                        # print('investigating', newR, newC, node.children[letter])
                        investigateCell(newR, newC, node.children[letter], currStr + letter)
            
            board[r][c] = letter
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] in root.children):
                    investigateCell(i, j, root, "")

        return list(foundWords)                     

