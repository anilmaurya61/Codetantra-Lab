package q10823;
public class CorrectUsageOfNaN{
	public static void main(String[]args){
		Double x=2.0%0;
		System.out.println("x == Double.NaN : "+(x==Double.NaN));
		System.out.println("Double.isNaN(x) : "+(Double.isNaN(x)));
	}
}