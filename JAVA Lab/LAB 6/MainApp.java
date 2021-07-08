package q11284;

interface Car {
        public String getName();

        public int getMaxSpeed();

        public default void applyBreak(){
                System.out.println("Applying break on " + getName());
        }

        public static Car getFastestCar(Car car1, Car car2){
                return car1.getMaxSpeed() > car2.getMaxSpeed() ? car1: car2;
        }
}
class BMW implements Car {
        private int maxSpeed;
        private String name;

        BMW(int speed, String name){
                this.maxSpeed = speed;
                this.name = name;
        }

        public String getName(){
                return name;
        }

        public int getMaxSpeed(){
                return maxSpeed;
        }

}
class Audi implements Car {
        private String name;
        private int maxSpeed;

        Audi(int speed, String name){
                this.maxSpeed =speed;
                this.name = name;
        }

        public int getMaxSpeed(){
                return maxSpeed;
        }

        public String getName(){
                return name;
        }


}
public class MainApp {
        public static void main(String args[]) {
                BMW b = new BMW(Integer.parseInt(args[1]), args[0]);
                Audi a = new Audi(Integer.parseInt(args[3]), args[2]);

                System.out.println("Fastest car is : " + Car.getFastestCar(b, a).getName());
        }
}
