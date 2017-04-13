import java.io.*;
import java.util.*;
import java.util.stream.*;

public class Solution {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(in.readLine());

        IntStream.range(1, num + 1)
                 .forEach(e -> {
                        IntStream.range(e, num)
                                 .forEach(space -> System.out.print(" "));
                        IntStream.range(0, e)
                                 .map(i -> -1 - i + num -1)
                                 .forEach(inner_e -> System.out.print("#"));
                        System.out.println();
                 });
    }
}
