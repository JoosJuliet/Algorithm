package project;
import java.util.*;

public class Main {

	ArrayList<Integer> binArray = new ArrayList<Integer>();
	Scanner sc = new Scanner(System.in);

	public Main(){
		System.out.print("Input Decimal Number : ");
		int decimalNumber = sc.nextInt();
		convert(decimalNumber);
		printResult();
	}

	public void convert(int decimalNumber){
		int currentValue = decimalNumber;
		while(currentValue >0){
			binArray.add(currentValue%2);
			currentValue = currentValue/2;
		}
	}

	public void printResult(){
		for(int idx = binArray.size() -1; idx>=0; idx--){
			System.out.print(binArray.get(idx)+" ");
		}
	}

	public static void main(String[] args){
		new Main();
	}
}
