class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0
        elif endWord==beginWord:
            return 1
        graph={}
        for word in wordList:
            for k in range(len(word)):
                graph[word[:k]+'*'+word[k+1:]]=graph.get(word[:k]+'*'+word[k+1:],[])+[word]
        startqueue=[{beginWord}]
        endqueue=[{endWord}]
        count=1
        visit1=set()
        visit1.add(beginWord)
        visit2=set()
        visit2.add(endWord)
        while startqueue and endqueue:
            nodes1=startqueue.pop()
            nextnodes1=set()
            nodes2=endqueue.pop()
            nextnodes2=set()
            print(nodes2,nodes1)
            count+=1
            for node1 in nodes1:
                for i in range(len(node1)):
                    if node1[:i]+'*'+node1[i+1:] in graph:
                        for word1 in graph[node1[:i]+'*'+node1[i+1:]]:
                            if word1 not in visit1:
                                visit1.add(word1)
                                nextnodes1.add(word1)
                            if word1 in visit2:
                                return count
            count+=1
            for node2 in nodes2:
                for i in range(len(node2)):
                    if node2[:i]+'*'+node2[i+1:] in graph:
                        for word2 in graph[node2[:i]+'*'+node2[i+1:]]:
                            if word2 not in visit2:
                                visit2.add(word2)
                                nextnodes2.add(word2)
                            if word2 in visit1:
                                return count
            if nextnodes1:
                startqueue.append(nextnodes1)
            if nextnodes2:
                endqueue.append(nextnodes2)
        return 0