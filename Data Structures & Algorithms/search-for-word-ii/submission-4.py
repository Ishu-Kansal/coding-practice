class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        if not board or not board[0]:
            return []

        # Build Trie
        root = {}
        END = "$"

        for word in words:
            node = root

            for ch in word:
                node = node.setdefault(ch, {})

            node[END] = word

        rows, cols = len(board), len(board[0])

        DIRECTIONS = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        results = []

        def dfs(r, c, parent):

            letter = board[r][c]

            # Does this character exist in the current Trie node?
            node = parent.get(letter)

            if node is None:
                return

            # Have we found a complete word?
            word = node.pop(END, None)

            if word is not None:
                results.append(word)

            # Mark current cell as visited
            board[r][c] = '#'

            # Explore neighbors
            for dr, dc in DIRECTIONS:

                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and
                    0 <= nc < cols and
                    board[nr][nc] != '#'):

                    dfs(nr, nc, node)

            # Restore board
            board[r][c] = letter

            # Prune exhausted Trie branches
            if not node:
                parent.pop(letter)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root:
                    dfs(r, c, root)

        return results