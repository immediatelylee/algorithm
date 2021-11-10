import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class backjun_2588Multiple {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // String[] str = br.readLine().split(" ");
        int a = Integer.parseInt(br.readLine());
        int b = Integer.parseInt(br.readLine());

        System.out.println(a * (b % 10));
        System.out.println(a * (b / 10 % 10));
        System.out.println(a * (b / 100));
        System.out.println(a * b);
    }

}
