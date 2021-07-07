package q11269;

class A {
        int a;

        public A(int a){
                this.a = a;
        }

        int getAValue(){
                return a;
        }
}

class B extends A{
        int b;
        public B(int a, int b){
                super(a);
                this.b = b;
        }

        int getBValue(){
                return b;
        }

}

public class InheritanceExample{
        public static void main(String[] args){
                B b = new B(4, 3);
                A a1 = new A(2), a2 = new A(4);
                System.out.println("a1.getAValue() : "+ a1.getAValue());
                System.out.println("b.getBValue() : " + b.getBValue());
                System.out.println("b.getAValue() : " + b.getAValue());
                System.out.println("a2.getAValue() : " + a2.getAValue());
        }
}
