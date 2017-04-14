import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.function.*;
import java.util.stream.*;

public class Solution {

    public static final int getCurrLocation(final int startingLocation, final int velocity, final int jumpNumber) {
        return startingLocation + velocity * jumpNumber;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        final int x1 = in.nextInt();
        final int v1 = in.nextInt();
        final int x2 = in.nextInt();
        final int v2 = in.nextInt();

        final List<Integer> velocities = Arrays.asList(v1, v2);
        final List<Integer> locations = Arrays.asList(x1, x2);

        final Predicate<Integer> landOnSameSpace =
            jumpNum -> getCurrLocation(x1, v1, jumpNum) == getCurrLocation(x2, v2, jumpNum);

        System.out.println(
            IntStream.range(0, 5000)
                     .noneMatch(e -> landOnSameSpace.test(e))
                     ? "NO" : "YES"
        );
    }
}
