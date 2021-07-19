import java.util.Scanner;

public class Main {

    static class Treap{
        final int INF = 100000000;
        private class Node{
            public int key;
            public double weight;
            public int rank,cnt;
            public Node left,right;
            public Node(int key){
                this.key=key;
                weight=Math.random();
                rank=1;
                cnt=1;
                left=null;
                right=null;
            }
            public int get_leftRank(){
                if (left==null){
                    return 0;
                }
                return left.rank;
            }
            public int get_rightRank(){
                if (right==null){
                    return 0;
                }
                return right.rank;
            }
            public void calRank(){
                rank=get_leftRank()+get_rightRank()+cnt;
            }
        }
        public Node root;
        public Treap(){
            root=null;
        }
        public void add(int key){
            root=add(root,key);
        }
        private Node right_rotate(Node a){
            Node b=a.left;
            a.left=b.right;
            b.right=a;
            a.calRank();
            b.calRank();
            return b;
        }
        private Node left_rotate(Node a){
            Node b=a.right;
            a.right=b.left;
            b.left=a;
            a.calRank();
            b.calRank();
            return b;
        }
        private Node add(Node node,int key){
            if (node==null){
                return new Node(key);
            }
            if (key==node.key){
                node.cnt++;
            }else if(key<node.key){
                node.left=add(node.left,key);
                if(node.left.weight<node.weight){
                    node=right_rotate(node);
                }
            }else {
                node.right=add(node.right,key);
                if(node.right.weight<node.weight){
                    node=left_rotate(node);
                }
            }
            node.calRank();
            return node;
        }
        public void remove(int key){
            root=remove(root,key);

        }
        public Node remove(Node node,int key){
            if (node==null){
                return null;
            }
            if (node.key==key){
                if(node.cnt>1){
                    node.cnt-=1;
                }else {
                    if (node.left==null){
                        return node.right;
                    }else if(node.right==null){
                        return node.left;
                    }else {
                        if(node.left.weight<node.right.weight){
                            node=right_rotate(node);
                            node.right=remove(node.right,key);
                        }else {
                            node=left_rotate(node);
                            node.left=remove(node.left,key);
                        }
                    }
                }
            }else if(key<node.key){
                node.left=remove(node.left,key);
            }else {
                node.right=remove(node.right,key);
            }
            if (node!=null){
            node.calRank();
            return node;}
            return null;
        }

        public int getRankByVal(int val){
            return getRankByVal(root,val);
        }
        private int getRankByVal(Node node,int val){
            if (node!=null){
                if (val>node.key){
                    return node.get_leftRank()+node.cnt+getRankByVal(node.right,val);
                }else if (val==node.key){
                    return node.get_leftRank()+1;
                }else {
                    return getRankByVal(node.left,val);
                }
            }
            return 0;
        }
        public int getValByRank(int rank){
            return getValByRank(root,rank);
        }
        private int getValByRank(Node node,int rank){
            if (node!=null){
                if (rank<=node.get_leftRank()){
                    return getValByRank(node.left,rank);
                }else if(rank<=node.get_leftRank()+node.cnt){
                    return node.key;
                }else {
                    return getValByRank(node.right,rank-node.get_leftRank()-node.cnt);
                }
            }
            return INF;
        }
        public int getPre(int val){
            return getPre(root,val);
        }
        private int getPre(Node node, int x){
            if(node==null) return -INF;
            if(x<=node.key) return getPre(node.left, x);
            return Math.max(node.key, getPre(node.right, x));
        }

        public int getNext(int val){
            return getNext(root,val);
        }
        private int getNext(Node node, int x){
            if(node==null) return INF;
            if(x>=node.key) return getNext(node.right, x);
            return Math.min(node.key, getNext(node.left, x));
        }
    }

    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Treap tree=new Treap();
        while(n-->0){
            int op = in.nextInt();
            int val = in.nextInt();
            if (op==1){
                tree.add(val);
            }else if(op==2){
                tree.remove(val);
            }else if(op==3){
                System.out.println(tree.getRankByVal(val));
            }else if(op==4){
                System.out.println(tree.getValByRank(val));
            }else if(op==5){
                System.out.println(tree.getPre(val));
            }else{
                System.out.println(tree.getNext(val));
            }
        }
    }
}
