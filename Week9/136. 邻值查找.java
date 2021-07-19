import java.util.Scanner;
public class Main {
    static final boolean RED = true;
    static final boolean BLACK = false;
    static final int MAXINF = Integer.MAX_VALUE;
    static int prkey;
    static int nxkey;
    static final int minf = Integer.MIN_VALUE;
    static int ans;
    static int result;
    static class RBTree{
        class Node{
            public int key,val;
            public Node left, right;
            public boolean color;

            public Node(int key,int value){
                this.key = key;
                val=value;
                left = null;
                right = null;
                color = RED;
            }
        }
        public Node root;
        public RBTree(){
            root = null;
        }
        private boolean isRed(Node node){
            if(node == null)
                return BLACK;
            return node.color;
        }
        private Node leftRotate(Node node){
            Node x = node.right;
            // 左旋转
            node.right = x.left;
            x.left = node;
            x.color = node.color;
            node.color = RED;
            return x;
        }
        private Node rightRotate(Node node){

            Node x = node.left;
            // 右旋转
            node.left = x.right;
            x.right = node;

            x.color = node.color;
            node.color = RED;
            return x;
        }
        private void flipColors(Node node){

            node.color = RED;
            node.left.color = BLACK;
            node.right.color = BLACK;
        }
        public void add(int key,int val){
            root = add(root, key,val);
            root.color = BLACK; // 最终根节点为黑色节点
        }

        // 返回插入新节点后红黑树的根
        private Node add(Node node, int key,int val){

            if(node == null){
                return new Node(key,val); // 默认插入红色节点
            }
            if(val<node.val)
                node.left = add(node.left, key,val);
            else
                node.right = add(node.right, key,val);
            if (isRed(node.right) && !isRed(node.left))
                node = leftRotate(node);

            if (isRed(node.left) && isRed(node.left.left))
                node = rightRotate(node);

            if (isRed(node.left) && isRed(node.right))
                flipColors(node);
            return node;
        }
        public int[] getPre(int val){
            ans=minf;
            prkey=-1;
            getPre(root,val);
            return new int[]{prkey,ans};
        }
        private void getPre(Node node,int val){
            if (node!=null){
                if(val==node.val){
                    if(node.left!=null){
                        Node cur =node.left;
                        while(cur.right!=null){
                            cur=cur.right;
                        }
                        ans=cur.val;
                        prkey=cur.key;
                    }
                }else if(val>node.val){
                    if(ans<node.val){
                        ans=node.val;
                        prkey=node.key;
                    }else if((ans==node.val) && (node.key<prkey)){
                        prkey=node.key;
                    }
                    getPre(node.right,val);
                }else{
                    getPre(node.left,val);
                }
            }
        }
        public int[] getNext(int val){
            result=MAXINF;
            nxkey=-1;
            getnext(root,val);
            return new int[]{nxkey,result};
        }
        private void getnext(Node node,int val){
            if (node!=null){
                if(val<node.val){
                    if (node.val<result) {
                        result = node.val;
                        nxkey=node.key;
                    }else if((node.val==result) && (node.key<nxkey)){
                        nxkey=node.key;
                    }
                    getnext(node.left,val);
                }else if(val==node.val){
                    if(node.right!=null){
                        Node cur=node.right;
                        while(cur.left!=null){
                            cur=cur.left;
                        }
                        result=cur.val;
                        nxkey=cur.key;
                    }
                }else{
                    getnext(node.right,val);
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        RBTree tree=new RBTree();
        int cnt=1;
        tree.add(cnt,in.nextInt());
        while (--n>0){
            cnt++;
            int v=in.nextInt();
            tree.add(cnt,v);
            int[] leftnum=tree.getPre(v);
            int[] rightnum=tree.getNext(v);
            int leftdis=Math.abs(v-leftnum[1]);
            int rightdis=Math.abs(rightnum[1]-v);
            if (leftdis<rightdis){
                System.out.println(leftdis+" "+leftnum[0]);
            }else if(leftdis>rightdis){
                System.out.println(rightdis+" "+rightnum[0]);
            }else{
                if (leftnum[1]<rightnum[1]){
                    System.out.println(leftdis+" "+leftnum[0]);
                }else {
                    System.out.println(rightdis+" "+rightnum[0]);
                }
            }
        }
    }
}
