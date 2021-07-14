import java.util.ArrayList;
class Solution {
public class RBTree{
    private static final boolean RED = true;
    private static final boolean BLACK = false;
    private class Node{
        public int key;
        public int value;
        public Node left, right;
        public boolean color;
        public Node(int key, int value){
            this.key = key;
            this.value = value;
            left = null;
            right = null;
            color = RED;
        }
    }
    private Node root;
    private int size;
    public RBTree(){
        root = null;
        size = 0;
    }
    public int getSize(){
        return size;
    }
    public boolean isEmpty(){
        return size == 0;
    }

    // 判断节点node的颜色
    private boolean isRed(Node node){
        if(node == null)
            return BLACK;
        return node.color;
    }

    //   node                     x
    //  /   \     左旋转         /  \
    // T1   x   --------->   node   T3
    //     / \              /   \
    //    T2 T3            T1   T2
    private Node leftRotate(Node node){

        Node x = node.right;

        // 左旋转
        node.right = x.left;
        x.left = node;

        x.color = node.color;
        node.color = RED;

        return x;
    }

    //     node                   x
    //    /   \     右旋转       /  \
    //   x    T2   ------->   y   node
    //  / \                       /  \
    // y  T1                     T1  T2
    private Node rightRotate(Node node){

        Node x = node.left;

        // 右旋转
        node.left = x.right;
        x.right = node;

        x.color = node.color;
        node.color = RED;

        return x;
    }

    // 颜色翻转
    private void flipColors(Node node){

        node.color = RED;
        node.left.color = BLACK;
        node.right.color = BLACK;
    }

    // 向红黑树中添加新的元素(key, value)
    public void add(int key, int value){
        root = add(root, key, value);
        root.color = BLACK; // 最终根节点为黑色节点
    }

    // 向以node为根的红黑树中插入元素(key, value)，递归算法
    // 返回插入新节点后红黑树的根
    private Node add(Node node, int key, int value){

        if(node == null){
            size ++;
            return new Node(key, value); // 默认插入红色节点
        }

        if(value<node.value)
            node.left = add(node.left, key, value);
        else
            node.right = add(node.right, key, value);

        if (isRed(node.right) && !isRed(node.left))
            node = leftRotate(node);

        if (isRed(node.left) && isRed(node.left.left))
            node = rightRotate(node);

        if (isRed(node.left) && isRed(node.right))
            flipColors(node);

        return node;
    }

    public int[] findMax(){
        Node node=maxmum(root);
        return new int[]{node.key,node.value};
    }

    private Node maxmum(Node node){
        if(node.right==null){
            return node;
        }
        return maxmum(node.right);
    }
    public void extractMax(){
        root=removeMax(root);
    }

    private Node removeMax(Node node){
        if(node.right==null){
            Node rightNode=node.left;
            node.left=null;
            size--;
            return rightNode;
        }
        node.right=removeMax(node.right);
        return node;
    }

    // 返回以node为根的二分搜索树的最小值所在的节点
    private Node minimum(Node node){
        if(node.left == null)
            return node;
        return minimum(node.left);
    }


    private Node removeMin(Node node){
        if(node.left == null){
            Node rightNode = node.right;
            node.right = null;
            size --;
            return rightNode;
        }
        node.left = removeMin(node.left);
        return node;
    }


}
    public int[] maxSlidingWindow(int[] nums, int k) {
        RBTree tree=new RBTree();
        int[] res=new int[nums.length-k+1];
        int []temp;
        for(int i=0;i<nums.length;i++){
                tree.add(i,nums[i]);
                if(i>=k-1){
                    while (true){
                        temp=tree.findMax();
                        if(i-temp[0]>=k){
                            tree.extractMax();    
                        }else{
                            break;
                        }
                    }
                    res[i-k+1]=temp[1];
                }
        }
        return res;
    }
}