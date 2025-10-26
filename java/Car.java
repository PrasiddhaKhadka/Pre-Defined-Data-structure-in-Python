public class Car{
    String model;
    int year;
    String color;
    int seats;
    int fuel_capacity;
    String fuel_type;

    public Car(String model, int year, String color, int seats, int fuel_capacity, String fuel_type){
        // object intilz
        this.model = model;
        this.year = year;
        this.color = color;
        this.seats = seats;
        this.fuel_capacity = fuel_capacity;
        this.fuel_type = fuel_type;
    }

    void displayProperties(){
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
        System.out.println("Color: " + color);
        System.out.println("Seats: " + seats);
        System.out.println("Fuel Capacity: " + fuel_capacity);
        System.out.println("Fuel Type: " + fuel_type);
    }

    void drive(){
        System.out.println("Driving the car...");
    }
}


class Test{
    public static void main(String[] args){
        Car car1 = new Car("Toyota", 2022, "Red", 5, 50, "Gasoline");
        car1.displayProperties();
        
        car1.drive();
    }
}
