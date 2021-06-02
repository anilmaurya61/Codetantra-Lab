package q11075;
import java.util.Scanner;

public class CountOfTwoNumbers {
	/**
	 * Find the count of arg1 is more than arg2 in the arr or not 
	 * 
	 * 
	 * 
	 * @return result
	 */ 
	 
	
	public boolean compareCountOf(int[] arr, int arg1, int arg2) {
		//write your code here
		if(arg1==arg2){
			return false;
		}
		int n=arr.length;
		int count1=0;
		int count2=0;
		for(int i=0;i<n;i++){
			if(arr[i]==arg1){
				count1++;
			}else if(arr[i]==arg2){
				count2++;
			}
		}
		return count1>count2;
		
	}
}