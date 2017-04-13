import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws IOException {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
       BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

       in.readLine();
       String numbers = in.readLine();

       System.out.println(
            Arrays.asList(numbers.split("\\s+"))
                  .stream()
                  .map(e -> Long.parseLong(e))
                  .reduce((e1, e2) -> e1 + e2)
                  .get()
           );
    }
}
