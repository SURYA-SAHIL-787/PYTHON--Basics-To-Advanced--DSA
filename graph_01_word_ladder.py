from collections import deque

def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)

    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps

        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                newWord = word[:i] + ch + word[i+1:]

                if newWord in wordSet:
                    queue.append((newWord, steps + 1))
                    wordSet.remove(newWord)

    return 0


# Example
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(ladderLength(beginWord, endWord, wordList))
