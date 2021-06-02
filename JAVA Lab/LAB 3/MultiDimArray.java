package q10946;
import java.util.Scanner;
public class MultiDimArrayPrinter{
	public static void main(String[] args){
	
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter Number of rows: ");
		int r=sc.nextInt();
		System.out.print("Enter Number of columns: ");
		int c=sc.nextInt();
		int arr[][]=new int[r][c];
		for(int i=0;i<r;i++){
			System.out.print("Enter row "+(i+1)+": ");
			for(int j=0;j<c;j++){
				arr[i][j]=sc.nextInt();
			}
		}
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
		
	}
}