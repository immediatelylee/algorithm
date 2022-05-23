
// https://www.acmicpc.net/problem/11047
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class a_1_conin0 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int cnt = 0;
        int[] coin_list = new int[n];

        for (int i = 0; i < n; i++) {
            coin_list[i] = Integer.parseInt(br.readLine());
        }

        for (int i = n - 1; i >= 0; i--) {
            if (k >= coin_list[i]) {
                cnt += k / coin_list[i];
                k = k % coin_list[i];
            }
        }
        System.out.println(cnt);
    }
}
