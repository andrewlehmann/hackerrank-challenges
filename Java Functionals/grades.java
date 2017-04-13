import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.stream.*;

public class Solution {


    static boolean roundChecker(int number) {
        return IntStream.rangeClosed(number, number + 2)
                        .filter(e -> e >= 38)
                        .filter(e -> e % 5 == 0)
                        .count() > 0
            && ((number % 5 != 0));
    }

    static Integer calculateRounded(int number) {
        return roundChecker(number) ? (number + 5 - (number % 5)) : number;
    }

    static List<Integer> solve(Integer[] grades){
        List<Integer> numbers = Arrays.asList(grades);

        return numbers.stream()
                      .map(e -> calculateRounded(e))
                      .collect(Collectors.toList());

    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Integer[] grades = new Integer[n];
        for(int grades_i=0; grades_i < n; grades_i++){
            grades[grades_i] = in.nextInt();
        }
        List<Integer> result = solve(grades);
        result.stream()
              .forEach(System.out::println);
    }
}
