import java.io.*;
import java.util.*;

public class Solution {
    
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(in.readLine());
        
        IntStream(0, num).forEach(e -> {
            IntStream(0, e).forEach(inner_e ->
                                               System.out.print("#"));
            System.out.println();
        });
    }
}