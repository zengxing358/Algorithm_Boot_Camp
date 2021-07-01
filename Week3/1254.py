"""
https://leetcode-cn.com/problems/tree-diameter/
先转为N叉树，再计算N叉树直径
"""

class Tree:
    def __init__(self,val,children):
        self.val=val
        self.children=children
class Solution:
    def treeDiameter(self, edges) :
        son=set()
        dic={}
        for first,second in edges:
            if first not in dic and second not in dic:
                node=Tree(first,[])
                dic[first]=node
                child=Tree(second,[])
                dic[second]=child
                node.children.append(child)
                son.add(second)
            elif first not in dic:
                node=dic[second]
                child=Tree(first,[])
                node.children.append(child)
                dic[first]=child
                son.add(first)
            else:
                node=dic[first]
                child=Tree(second,[])
                dic[second]=child
                node.children.append(child)
                son.add(second)
        father=set(range(len(edges)+1))-son
        root=dic[father.pop()]
        return self.diameter(root)
    def diameter(self, root) -> int:
        if root is None:
            return 0
        ans = [0]
        #  返回所有root节点到叶子节点的路径的最长长度
        def dfs(root):
            if len(root.children) == 0:
                return 0
            # 最大值和次大值
            max1, max2 = 0, 0
            for child in root.children:
                length = dfs(child)
                if length+1 > max1:
                    max2 = max1
                    max1 = length+1
                elif length+1 > max2:
                    max2 = length+1
            ans[0] = max(ans[0], max1 + max2)
            return max1
        dfs(root)
        return ans[0]