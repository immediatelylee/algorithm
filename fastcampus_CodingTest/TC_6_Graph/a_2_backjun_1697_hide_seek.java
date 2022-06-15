import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import java.util.LinkedList;
import java.util.Queue;

public class a_2_backjun_1697_hide_seek {
    static int MAX = 100001;
    static int[] visited = new int[MAX];
    static int N;
    static int K;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        int result = bfs(N);
        System.out.println(result);
        // System.out.println(Arrays.toString(visit)); 배열출력
    }

    private static int bfs(int node) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(node);
        int index = node;
        int n = 0;
        visited[index] = 1;
        while (queue.isEmpty() == false) {
            n = queue.remove();
            if (n == K) {
                return visited[n] - 1;
            }
            if (n - 1 >= 0 && visited[n - 1] == 0) {
                visited[n - 1] = visited[n] + 1;
                queue.add(n - 1);
            }
            if (n + 1 <= 100000 && visited[n + 1] == 0) {
                visited[n + 1] = visited[n] + 1;
                queue.add(n + 1);
            }
            if (2 * n <= 100000 && visited[2 * n] == 0) {
                visited[2 * n] = visited[n] + 1;
                queue.add(2 * n);
            }
        }

        return -1;

    }

}