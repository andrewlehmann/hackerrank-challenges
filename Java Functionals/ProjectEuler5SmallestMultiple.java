import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.stream.*;

public class Solution {

    public static Integer flattenByMult(final int number) {
        return IntStream.rangeClosed(1, number)
                        .reduce((num1, num2) -> num1 * num2)
                        .getAsInt();
    }
   public static boolean findMinDivisible(int upperLimit, int number) {
        return IntStream.rangeClosed(1, upperLimit)
                        .allMatch(e -> number % e == 0);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        List<Integer> numbers = 
            in.lines()
              .map(Integer::parseInt)
              .collect(Collectors.toList());

      List<Integer> flatMaxValue = 
            numbers.stream()
                   .map(Solution::flattenByMult)
                   .collect(Collectors.toList());
  
      flatMaxValue.stream()
                       .forEach(e ->
                            System.out.println(
                               IntStream.rangeClosed(1, e)
                                        .filter(f -> 
                                            findMinDivisible(
                                                numbers.get(flatMaxValue.indexOf(e)), f))
                                        .findFirst()
                                        .getAsInt()
                                ));
    }
}
