class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree=self.dic
        for w in word:
            if w not in tree:
                tree[w]={}
            tree=tree[w]
        tree['#']=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree=self.dic
        for w in word:
            if w not in tree:
                return False
            tree=tree[w]
        if '#' in tree:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree=self.dic
        for pre in prefix:
            if pre not in tree:
                return False
            tree=tree[pre]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)