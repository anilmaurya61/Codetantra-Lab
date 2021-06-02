package q10894;

public class NumberPalindrome {
	
	public void isNumberPalindrome(int number) {
		
		//Write your code her
		int n=number;
		int sum =0;
		int rem;
		while(n>0){
			rem=n%10;
			sum=(sum*10)+rem;
			n=n/10;
		}
		if(sum== number){
			System.out.println(number+" is a palindrome");
			
		}
		else{
			System.out.println(number+" is not a palindrome");
		}
	}
}