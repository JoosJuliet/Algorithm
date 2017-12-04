package project;

import java.util.Scanner;
 

public class Main {

    /**
     * @param args
     */

    public static void main(String[] args) {
        String[] numArray = {"","","이","삼","사","오","육","칠","팔","구"};
        String[] decimal = {"","십","백","천","만"};

        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();           

        StringBuilder sb = new StringBuilder(99999); // Capacity:200, length:0

        if( sb.length() > 5){
            System.out.println("범위가 초과되었습니다.");
        }

        sb.append(input); // Capacity:200, length:5

        if( sb.toString().equals("0") ){
            System.out.println("영");
            return;
        }

        String answr = "";
			
        for (int i = 0; i < sb.length(); i++) {
			if(  (sb.charAt(i) == '1') && (i == (sb.length()-1))) {
				answr += "일";   
			}else{
				answr += numArray[sb.charAt(i)-'0']+ decimal[sb.length()-(i+1)];
			}
        }
        System.out.println(answr);

    }
}
