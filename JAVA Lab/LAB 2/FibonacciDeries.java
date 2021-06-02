package q10896;
public class FibonacciSeries{
	public static void main(String[]args){
		int n=Integer.parseInt(args[0]);
		int n0=0,n1=1,n2;
		if(n<0 || n==0){
			System.out.println("Not possible!");
		}
		else if(n==1){
			System.out.println(n0);
		}
		else{
			System.out.print(n0+" "+n1);
			for(int i=2;i<n;i++){
				n2=n0+n1;
				n0=n1;
				n1=n2;
				if(n2>n){
					break;
				}else{
					System.out.print(" "+n2);
				}
			}
		}
	}
}