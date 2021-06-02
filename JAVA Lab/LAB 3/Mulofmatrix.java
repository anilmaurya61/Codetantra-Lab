package q11106;
public class MultiplicationOfMatrix{
	public int[][] multiplication(int[][] matrix1, int[][] matrix2) {
		/*Return the result if the matrix1 coloumn size is equal to matrix2 row size and print the result.
		* @Return null.
		*/
		// Write your logic here for matrix multiplication
		int result[][]=new int[matrix1.length][matrix2[1].length];
		if(matrix1[1].length!=matrix2.length){
			return null;
		}
		else{
			
			for(int i=0;i<matrix1.length;i++){
				for(int j=0;j<matrix2[1].length;j++){
					for(int k=0;k<matrix2.length;k++){
					result[i][j]+=matrix1[i][k]*matrix2[k][j];
					}
				}
			}
			return result;
		}
	}
}