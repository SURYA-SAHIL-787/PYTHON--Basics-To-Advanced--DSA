class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def build_trie(words):
    root = TrieNode()

    for word in words:
        node = root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = word

    return root


def dfs(board, r, c, node, result):
    if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] == '#':
        return

    ch = board[r][c]
    if ch not in node.children:
        return

    next_node = node.children[ch]

    if next_node.word:
        result.append(next_node.word)
        next_node.word = None   # avoid duplicates

    board[r][c] = '#'

    dfs(board, r + 1, c, next_node, result)
    dfs(board, r - 1, c, next_node, result)
    dfs(board, r, c + 1, next_node, result)
    dfs(board, r, c - 1, next_node, result)

    board[r][c] = ch


def find_words(board, words):
    root = build_trie(words)
    result = []

    for r in range(len(board)):
        for c in range(len(board[0])):
            dfs(board, r, c, root, result)

    return result


board = [
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]

words = ["oath", "pea", "eat", "rain", "hike"]

print(find_words(board, words))
