import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int r= scn.nextInt();
        int c= scn.nextInt();
        printKnightsTour(new int[n][n],r,c,1);
    }

    public static void printKnightsTour(int[][] chess, int r, int c, int upcomingMove) {
        System.out.println(chess.length);
        if(r < 0 || c < 0 || r >= chess.length || c >= chess.length || chess[r][c] > 0){
            return;
        }
        if(upcomingMove == chess.length * chess.length){
            chess[r][c] = upcomingMove;
            displayBoard(chess);
            chess[r][c] = 0;
            return;
        }
        int[][] dirn ={{-2,1},{-1,2},{1,2},{2,1},{2,-1},{1,-2},{-1,-2},{-2,-1}};
        chess[r][c]=upcomingMove;
        for(int[] d: dirn){
            printKnightsTour(chess,r+d[0],c+d[1],upcomingMove+1);
        }
        chess[r][c]=0;
    }

    public static void displayBoard(int[][] chess){
        for(int i = 0; i < chess.length; i++){
            for(int j = 0; j < chess[0].length; j++){
                System.out.print(chess[i][j] + " ");
            }
            System.out.println();
        }

        System.out.println();
    }
}