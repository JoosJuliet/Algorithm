// 약수구하기


import java.util.*;
public class Main {
	static Scanner s ;
	static String answer;
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Main myMain = new Main();
		s = new Scanner(System.in);
    int num = s.nextInt();

		if( num < 0 )
			System.out.println("음수는 받지 않습니다");
   else
   {
			int i;
			for(i =1; i<=num ; i++)
				if(num% i == 0)
					System.out.print(i+" ");
		}
	}
}
