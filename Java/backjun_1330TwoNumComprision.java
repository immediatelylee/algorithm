import java.io.BufferedReader;
import java.io.IOException;
import java.util.StringTokenizer;

import java.io.InputStreamReader;

public class backjun_1330TwoNumComprision {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        System.out.println((a > b) ? (">") : ((a < b) ? ("<") : ("==")));
    }
}
