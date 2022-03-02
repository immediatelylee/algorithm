import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class backjun_8393sum {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());

        int result = 0;
        for (int i = 1; i <= a; i++) {
            result = result + i;
        }

        System.out.println(result);
    }

}
