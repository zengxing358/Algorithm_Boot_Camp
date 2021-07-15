//红黑树
import java.util.Scanner;
public class Main {
    static class Node{
        public int key;
        public Node left, right;
        public boolean color;
        public int rank,count;
        public Node(int key){
            this.key = key;
            left = null;
            right = null;
            color = RED;
            rank=1;
            count=1;
        }
    }
    static final int INF = 100000000;
    static Node root;
    static final boolean RED = true;
    static final boolean BLACK = false;
    static void build(){
        root = null;
    }
    static void reCal(Node node){
        if(node!=null){
        node.rank=calRank(node);}
    }
    static int getRank(Node node){
        if (node==null){
            return 0;
        }
        return node.rank;
    }
    static int calRank(Node node){
        return getRank(node.left)+getRank(node.right)+node.count;
    }
    // 判断节点node的颜色
    static boolean isRed(Node node){
        if(node == null)
            return BLACK;
        return node.color;
    }
    //   node                     x
    //  /   \     左旋转         /  \
    // T1   x   --------->   node   T3
    //     / \              /   \
    //    T2 T3            T1   T2
    static Node leftRotate(Node node){

        Node x = node.right;
        // 左旋转
        node.right = x.left;
        x.left = node;
        x.color = node.color;
        node.color = RED;
        reCal(node);
        reCal(x);
        return x;
    }

    //     node                   x
    //    /   \     右旋转       /  \
    //   x    T2   ------->   y   node
    //  / \                       /  \
    // y  T1                     T1  T2
    static Node rightRotate(Node node){

        Node x = node.left;

        // 右旋转
        node.left = x.right;
        x.right = node;

        x.color = node.color;
        node.color = RED;
        reCal(node);
        reCal(x);
        return x;
    }

    // 颜色翻转
    static void flipColors(Node node){

        node.color = RED;
        node.left.color = BLACK;
        node.right.color = BLACK;
    }

    static void add(int key){
        root = add(root, key);
        root.color = BLACK; // 最终根节点为黑色节点
        reCal(root);
    }

    // 返回插入新节点后红黑树的根
    static Node add(Node node, int key){

        if(node == null){
            return new Node(key); // 默认插入红色节点
        }

        if(key<node.key)
            node.left = add(node.left, key);
        else if(key>node.key)
            node.right = add(node.right, key);
        else {
            node.count++;
            reCal(node);
            return node;}

        if (isRed(node.right) && !isRed(node.left))
            node = leftRotate(node);

        if (isRed(node.left) && isRed(node.left.left))
            node = rightRotate(node);

        if (isRed(node.left) && isRed(node.right))
            flipColors(node);
        reCal(node);
        return node;
    }

    // 返回以node为根节点的二分搜索树中，key所在的节点
    static Node getNode(Node node, int key){

        if(node == null)
            return null;

        if(key==node.key){
            return node;}
        else if(key<node.key)
            return getNode(node.left, key);
        else
            return getNode(node.right, key);
    }

    // 返回以node为根的二分搜索树的最小值所在的节点
    static Node minimum(Node node){
        if(node.left == null)
            return node;
        return minimum(node.left);
    }
    // 删除掉以node为根的二分搜索树中的最小节点
    // 返回删除节点后新的二分搜索树的根
    static Node removeMin(Node node){

        if(node.left == null){
            Node rightNode = node.right;
            node.right = null;
            reCal(rightNode);
            return rightNode;
        }
        node.left = removeMin(node.left);
        reCal(node);
        return node;
    }
    // 从二分搜索树中删除键为key的节点
    static void remove(int key){

        Node node = getNode(root, key);
        if(node != null){
            root = remove(root, key);
            if(root!=null){
                reCal(root);
            }
        }

    }
    static Node remove(Node node, int key){

        if( node == null )
            return null;

        if( key<node.key ){
            node.left = remove(node.left , key);
            reCal(node);
            return node;
        }
        else if(key>node.key){
            node.right = remove(node.right, key);
            reCal(node);
            return node;
        }
        else{
            if(node.count>1){
            node.count--;
            reCal(node);
            return node;
            }

            // 待删除节点左子树为空的情况
            if(node.left == null){
                Node rightNode = node.right;
                node.right = null;
                reCal(rightNode);
                return rightNode;
            }

            // 待删除节点右子树为空的情况
            if(node.right == null){
                Node leftNode = node.left;
                node.left = null;
                reCal(leftNode);
                return leftNode;
            }

            // 待删除节点左右子树均不为空的情况

            // 找到比待删除节点大的最小节点, 即待删除节点右子树的最小节点
            // 用这个节点顶替待删除节点的位置
            Node successor = minimum(node.right);
            successor.right = removeMin(node.right);
            reCal(successor.right);
            successor.left = node.left;
            node.left = node.right = null;
            reCal(successor);
            return successor;
        }
    }

    static int getRankByVal(int val){
        return getRankByVal(root,val);
    }
    static int getRankByVal(Node node,int val){
        if (node!=null){
            if (val>node.key){
                return getRank(node.left)+node.count+getRankByVal(node.right,val);
            }else if (val==node.key){
                return getRank(node.left)+1;
            }else {
                return getRankByVal(node.left,val);
            }
        }
        return 0;
    }
    static int getValByRank(int rank){
        return getValByRank(root,rank);
    }
    static int getValByRank(Node node,int rank){
        if (node!=null){
            if (rank<=getRank(node.left)){
                return getValByRank(node.left,rank);
            }else if(rank<=getRank(node.left)+node.count){
                return node.key;
            }else {
                return getValByRank(node.right,rank-getRank(node.left)-node.count);
            }
        }
        return INF;
    }
    static int getPre(int val){
        return getPre(root,val);
    }
    static int getPre(Node node, int x){
        if(node==null) return -INF;
        if(x<=node.key) return getPre(node.left, x);
        return Math.max(node.key, getPre(node.right, x));
    }

    static int getNext(int val){
        return getNext(root,val);
    }
    static int getNext(Node node, int x){
        if(node==null) return INF;
        if(x>=node.key) return getNext(node.right, x);
        return Math.min(node.key, getNext(node.left, x));
    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        build();
        add(-INF);
        add(INF);
        while(n-->0){
            int op = in.nextInt();
            int val = in.nextInt();
            if (op==1){
                add(val);
            }else if(op==2){
                remove(val);
            }else if(op==3){
                System.out.println(getRankByVal(val)-1);
            }else if(op==4){
                System.out.println(getValByRank(val+1));
            }else if(op==5){
                System.out.println(getPre(val));
            }else{
                System.out.println(getNext(val));
            }
        }
    }
}
