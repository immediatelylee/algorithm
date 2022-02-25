import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class backjun_2884Clock {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        if (b >= 45) {
            b = b - 45;
        } else {
            a = a - 1;
            if (a == -1) {
                a = 23;
            }
            b = b + 60 - 45;
        }
        System.out.println(a + " " + b);
    }

}
