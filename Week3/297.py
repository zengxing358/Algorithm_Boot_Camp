class Codec:
    
    def serialize(self, root):
        if root:
            res=[]
            queue=[root]
            while queue:
                node=queue[0]
                queue=queue[1:]
                if node:
                    res.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res.append("None")
            return "["+",".join(res)+"]"
        return ""
    def deserialize(self, data):
        if data:
            lst=data[1:-1].split(",")
            root=TreeNode(int(lst[0]))
            queue=[root]
            cnt=1
            while cnt<len(lst):
                node=queue[0]
                queue=queue[1:]
                if lst[cnt]!="None":
                    node.left=TreeNode(int(lst[cnt]))
                    queue.append(node.left)
                cnt+=1
                if lst[cnt]!="None":
                    node.right=TreeNode(int(lst[cnt]))
                    queue.append(node.right)
                cnt+=1
            return root
        return