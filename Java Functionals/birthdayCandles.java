import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.stream.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Integer height[] = new Integer[n];
        for(int height_i=0; height_i < n; height_i++){
            height[height_i] = in.nextInt();
        }
        List<Integer> heightList = Arrays.asList(height);
        int max =
            heightList.stream()
                      .mapToInt(Integer::valueOf)
                      .max()
                      .getAsInt();
        System.out.println(
            heightList.stream()
                      .collect(Collectors.groupingBy(e -> Integer.valueOf(e), Collectors.counting()))
                      .get(max)
        );



    }
}
