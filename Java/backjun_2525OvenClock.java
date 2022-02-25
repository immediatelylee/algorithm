import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class backjun_2525OvenClock {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int time = Integer.parseInt(br.readLine());

        m = m + time;
        while (m >= 60) {
            m = m - 60;
            h = h + 1;
        }

        while (h >= 24) {
            h = h - 24;
        }

        System.out.println(h + " " + m);
    }

}
