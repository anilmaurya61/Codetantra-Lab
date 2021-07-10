package q24215;
public class StringbufferExample {
	public static void main (String args[]) {
		StringBuffer sb = new StringBuffer();
		System.out.println("Initial capacity is: "+sb.capacity());
		sb = new StringBuffer(args[0]);
		System.out.println("Capacity after passing parameter is: "+sb.capacity());
		StringBuffer sn = new StringBuffer(50);
		System.out.println("Creating a StringBuffer object with the given capacity: "+sn.capacity());
	}
}
