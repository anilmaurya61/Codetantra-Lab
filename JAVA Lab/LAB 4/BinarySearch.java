package q11045;
public class BinarySearch{
	public void binarySearch(int []a,int key){
		int l=0;
		int h=a.length-1;
		int m;
		int pos=0;
		while(l<=h){
			m=(l+h)/2;
			if(a[m]==key){
				pos=m;
				break;
			}
			else if(key>a[m]){
				l=m+1;
			}
			else{
				h=m-1;
			}
		}
		if(pos!=0)
			System.out.println("Search element "+key+" is found at position : "+pos);
		else
		  System.out.println("Search element "+key+" is not found");
	}
}