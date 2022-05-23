import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class a_3_atm {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] atm_time = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            atm_time[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(atm_time); // java 진짜 불편하다
        int sum = 0;
        int presum = 0;

        for (int i = 0; i < n; i++) {
            presum = presum + atm_time[i];
            sum = sum + presum;
        }
        System.out.println(sum);

    }
}
