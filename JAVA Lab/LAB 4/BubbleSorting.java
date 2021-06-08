package q11039;
public class BubbleSorting{
	public void bubbleSort(int[] arr){
		int n=arr.length;
		int temp=0;
		for(int i=0;i<n;i++){
			for(int j=1; j<n-i;j++){
				if(arr[j-1]>arr[j]){
					temp=arr[j-1];
					arr[j-1]=arr[j];
					arr[j]=temp;
				}
			}
		}
		for(int k=0;k<n;k++){
			System.out.println(arr[k]);
		}
	}
}