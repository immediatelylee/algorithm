import java.io.BufferedReader;

import java.io.IOException;
import java.io.InputStreamReader;

import java.util.StringTokenizer;

public class backjun_11022AplusB_8 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int sum = a + b;
            sb.append("Case #").append(i).append(": ").append(a).append(" + ").append(b).append(" = ").append(sum)
                    .append("\n");
        }
        System.out.println(sb.toString());
    }
}
