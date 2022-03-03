import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class backjun_2439StarPrint_2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringBuffer sb = new StringBuffer();
        for (int i = 1; i <= n; i++) {
            for (int j = n - 1; j >= 0; j--) {
                sb.append(i <= j ? " " : "*");
            }
            sb.append("\n");
        }
        System.out.print(sb.toString());
        br.close();
    }
}
