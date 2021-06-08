package q11044;

public class LinearSearch{
	int i;
	 public void linearSearch(int []array,int key) {
	 	int n = array.length;
	 	for(i=0;i<n;i++){
	 		if(array[i]==key){
	 		  System.out.println("Search element "+key+" is found at position : "+i);
	 		  break;
	 		}
	 	}
	 	if(i==n){
	 	System.out.println("Search element "+key+" is not found");
	 }
	 }

}
