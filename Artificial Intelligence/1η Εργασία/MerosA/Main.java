
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        State start;
        int K;
        try (Scanner in = new Scanner(System.in)) {
            System.out.print("Enter the number of missionaries and cannibals (N): ");
            int N = in.nextInt();
            System.out.print("Enter the boat capacity (M): ");
            int M = in.nextInt();
            start = new State('l', N, M);
            System.out.print("Enter the maximum number of crossings (K): ");
            K = in.nextInt();
        }
        long startTime = System.currentTimeMillis();
        State finalState = aStar.solve(start, K);
        long endTime = System.currentTimeMillis();
        double totalTime;
        if (finalState == null) {
            System.out.println("Not found solution."); 
        }else {
            State temp = finalState;
            ArrayList<State> tree = new ArrayList<>();
            tree.add(finalState);
            while (temp.getFather() != null) {
                tree.add(temp.getFather());
                temp = temp.getFather();
            }
            Collections.reverse(tree);
            for (State node : tree) {
                System.out.println(node);
            }
            System.out.println();
            totalTime=(double) (endTime - startTime) / 1000;
            System.out.printf("Time: %.3f sec", totalTime);
        }
    }

}
