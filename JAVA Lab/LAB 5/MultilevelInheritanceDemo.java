package q11264;
class Student{
	int id;
	String name;
	
	void setData(int id, String name){
		this.id = id;
		this.name = name;
	}
	
	void displayData(){
		System.out.println("Id : " + this.id + "\nName : " + this.name);
	}
}

class Marks extends Student {
	float javaMarks, cMarks, cppMarks;
	
	void setMarks(float j, float c, float cpp){
		this.javaMarks = j;
		this.cMarks = c;
		this.cppMarks = cpp;
	}
	
	void displayMarks(){
		System.out.println("Java marks : " + this.javaMarks);
		System.out.println("C marks : "+ this.cMarks);
		System.out.println("Cpp marks : "+ this.cppMarks);
	}
}

class Result extends Marks{
	float total,avg;
	void compute(){
		this.total = this.javaMarks + this.cMarks + this.cppMarks;
		this.avg = this.total / 3;
	}
	
	void showResult(){
		System.out.println("Total : " + this.total);
		System.out.println("Avg : " + this.avg);
	}
}

public class MultilevelInheritanceDemo{
	public static void main(String[] args){
		Result r = new Result();
		r.setData(Integer.parseInt(args[0]),args[1]);
		r.setMarks( Float.parseFloat(args[2]) , Float.parseFloat(args[3]) , Float.parseFloat(args[4]) );
		r.compute();
		r.displayData();
		r.displayMarks();
		r.showResult();
	}
}