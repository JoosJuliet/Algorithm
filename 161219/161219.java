import java.util.*;

public class Main {

    public static void main(String[] args) {
        int sum =0;
        double average = 0;

        Scanner s = new Scanner(System.in);

        int x = s.nextInt();
        int[] num = new int[x];

        for(int i = 0 ; i < num.length; i++){
            num[i] = s.nextInt();
        }

        for(int i= 0 ; i < num.length; i++){
            sum += num[i];
        }

        average = sum/num.length;

        System.out.print(Math.round(average));
    }
}
