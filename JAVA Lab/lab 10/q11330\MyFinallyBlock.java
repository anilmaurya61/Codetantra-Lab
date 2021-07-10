package q11330;
public class MyFinallyBlock {
	public static void main(String args[]){
		int a1 = Integer.parseInt(args[0]);
		int a2 = Integer.parseInt(args[1]);
		float b1 = Float.parseFloat(args[2]);
		float b2 = Float.parseFloat(args[3]);
		try{
			int r1 = a1/a2;
			System.out.println("Result of integer values division : "+r1);
		}
		catch(ArithmeticException e1){
			System.out.println("Inside the 1st catch block");
		}
		finally{
			System.out.println("Inside the 1st finally block");
		}
		try{
			float r2 = b1/b2;
			System.out.println("Result of float values division : "+ r2);
		}
		catch(ArithmeticException e){
			System.out.println("Inside the 2nd catch block");
		}
		finally{
			System.out.println("Inside the 2nd finally block");
		}
	}
}
