import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static String[][] board;
    private static int[] line;
    private static int[] column;
    private static int[][] block;
    public static int[] ones = new int[1 << 9];
    public static int N=9;

    public static void solveSudoku(String[][] board) {
        int c=0;
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j].charAt(0) == '.') {
                    c++;
                } else {
                    int digit = board[i][j].charAt(0) - '0' - 1;
                    flip(i, j, digit);
                }
            }
        }
        dfs(c);
    }
    public static int get(int i,int j){
        return  ~(line[i] | column[j] | block[i / 3][j / 3]) & 0x1ff;
    }

    public static boolean dfs( int cnt) {
        if (cnt==0) {
            return true;
        }

        int i = 0, j = 0;
        int mincnt=10;
        int mask=0;
        for(int x=0;x<N;x++){
            for(int y=0;y<N;y++) {
                if(board[x][y].charAt(0)=='.') {
                    int state = get(x, y);
                    if((ones[state] == 0)){
                        return false;
                    }
                    if (  (ones[state] < mincnt)) {
                        i = x;
                        j = y;
                        mincnt = ones[state];
                        mask=state;
                    }
                }
            }
        }
        for (; mask != 0 ; mask &= (mask - 1)) {
            int digitMask = mask & (-mask);
            int digit = Integer.bitCount(digitMask - 1);
            flip(i, j, digit);
            char t= (char)('0' +digit +  1);
            board[i][j] = Character.toString(t);
            if (dfs( cnt - 1)){
                return true;
            }
            flip(i, j, digit);
            board[i][j] =".";
        }
        return false;
    }

    public static void flip(int i, int j, int digit) {
        line[i] ^= (1 << digit);
        column[j] ^= (1 << digit);
        block[i / 3][j / 3] ^= (1 << digit);
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String in;
        for (int i = 0; i < 1 << N; i++) {
            for (int j = 0; j < N; j++) {
                ones[i] += i >> j & 1;
            }
        }
        while(true){
            in= sc.next();
            board = new String[N][N];
            line = new int[9];
            column = new int[9];
            block = new int[3][3];
            if (in.equals("end")){
                break;
            }
            for(int i=0;i<N;i++){
                board[i]=in.substring(i*9,i*9+9).split("");
            }
            solveSudoku(board);
            for(int i=0;i<N;i++){
                for(int j=0;j<N;j++){
                    System.out.print(board[i][j]);
                }
            }
            System.out.println();
        }
    }
}