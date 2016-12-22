import java.util.*;


public class main {

    public static void main(String[] args) {

        int count =0;

        Scanner s = new Scanner(System.in);

        int x = s.nextInt();
        int y = s.nextInt();

        for(int i =x ; i<=y; i++) {
            int sqrt = (int) Math.sqrt(i);
            if (sqrt * sqrt == i) {

                count += 1;

            } else {


            }


        }

        System.out.print(count);

    }
}
