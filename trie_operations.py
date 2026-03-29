class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def collect_words(self, node=None, prefix="", result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root

        if node.is_end_of_word:
            result.append(prefix)

        for char, next_node in node.children.items():
            self.collect_words(next_node, prefix + char, result)

        return result

    def words_with_prefix(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []

            current = current.children[char]

        return self.collect_words(current, prefix, [])


if __name__ == "__main__":
    trie = Trie()

    words = ["apple", "app", "apply", "bat", "ball", "batter", "cat"]
    for word in words:
        trie.insert(word)

    print("Search 'apple':", trie.search("apple"))
    print("Search 'appl':", trie.search("appl"))
    print("Starts with 'app':", trie.starts_with("app"))
    print("Starts with 'ba':", trie.starts_with("ba"))
    print("Words with prefix 'app':", trie.words_with_prefix("app"))
    print("Words with prefix 'bat':", trie.words_with_prefix("bat"))
