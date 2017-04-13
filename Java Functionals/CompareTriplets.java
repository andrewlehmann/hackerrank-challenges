import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.stream.*;

public class CompareTriplets {

    public static boolean compareInts(final int e, final List<Integer> otherList, final int index) {
        return e > otherList.get(index);
    }

    public static long getWins(final List<Integer> a, final List<Integer> b) {
        return IntStream.range(0, a.size())
                .filter(i -> a.get(i) > b.get(i))
                .count();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a0 = in.nextInt();
        int a1 = in.nextInt();
        int a2 = in.nextInt();
        int b0 = in.nextInt();
        int b1 = in.nextInt();
        int b2 = in.nextInt();
        List<Integer> aScores = Arrays.asList(a0, a1, a2);
        List<Integer> bScores = Arrays.asList(b0, b1, b2);

        System.out.println(getWins(aScores, bScores) + " " + getWins(bScores, aScores));



    }
}
