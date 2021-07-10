package q24212;
class Example{
	public static void main(String args[]){
		String s =new String(args[0]);
		System.out.print("The result is: ");
		for(int i =0 ;i<s.length();i++){
			if(Character.isUpperCase(s.charAt(i))){
				System.out.print(s.charAt(i));
			}
		}
		System.out.println();
	}
}
