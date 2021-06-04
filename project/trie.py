class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = "#"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.end] = self.end

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.end in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

    def all_words(self):
        '''
        return all the words in the trie
        '''
        node = self.root
        ans = []
        self._collect(node, '', ans)
        return ans

    def _collect(self, node, path, ans):
        for k in node:
            if k == self.end:
                ans.append(path)
                continue
            self._collect(node[k], path + k, ans)

    def words_with_prefix(self, prefix: str):
        '''
        return all possible words with common prefix
        '''
        node = self.root
        for c in prefix:
            if c not in node:
                return []
            node = node[c]
        ans = []
        self._words_with_prefix_helper(node, prefix, ans)
        return ans

    def _words_with_prefix_helper(self, node, prefix, ans):
        for k in node:
            if k == self.end:
                ans.append(prefix)
                continue
            self._words_with_prefix_helper(node[k], prefix + k, ans)

    def longest_prefix(self, s):
        ''''
        return longest prefix of s in the trie
        '''
        ans = ''
        if not s:
            return ans
        node = self.root
        for c in s:
            if c not in node:
                return ans
            node = node[c]
            ans += c
        return ans