public class Car extends Vehicle {
    String model;
    
    Car(String mode){
        this.model = model;
    }

    @Override
    public void honk() {
        super.honk();
        System.out.println("Poo! Poo!");
    }


    public static void main(String[] args){
        Car object1 = new Car("XYZ");
        System.out.println(object1.brand);
        object1.honk();
    }
}
