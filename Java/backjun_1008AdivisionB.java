import java.util.Scanner;

public class backjun_1008AdivisionB {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        sc.close();

        double da = (double) A;
        double db = (double) B;

        System.out.println(da / db);
    }

}
