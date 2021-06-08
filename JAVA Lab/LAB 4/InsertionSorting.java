package q11040;
public class InsertionSorting{
	public void insertionSort(int[] arr){
		int n=arr.length;
		for(int i=0;i<n;i++){
			int key=arr[i];
			int j=i-1;
			
			while(j>=0 && arr[j]>key){
				arr[j+1]=arr[j];
				j=j-1;
				
			}
			arr[j+1]=key;
			
		}
		for(int k=0;k<n;k++)
		System.out.println(arr[k]);
	}
}