public class Dog extends Animal {
    private String name;
    private int year;
    private String color;
    private int legs;
    private int speed;
    private String fuelType;

    // Constructor
    public Dog(String name, int year, String color, int legs, int speed, String fuelType) {
        this.name = name;
        this.year = year;
        this.color = color;
        this.legs = legs;
        this.speed = speed;
        this.fuelType = fuelType;
    }

    // Extra method to display details
    public void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Year: " + year);
        System.out.println("Color: " + color);
        System.out.println("Legs: " + legs);
        System.out.println("Speed: " + speed + " km/h");
        System.out.println("Fuel Type: " + fuelType);
        System.out.println("Inherited Breed: " + breed); // from Animal
    }

    // @Override
    // void animalSound(String name) {
    //     System.out.println("The dog barks " + name);
    // }

    @Override
    void animalEat() {
        super.animalEat();
        System.out.println("The dog eats meats");
    }

    // getter method 
    public String getDogName(){
        return name;
    }

    public static void main(String[] args) {
        Dog dog1 = new Dog("Golden Retriever", 2022, "White", 4, 50, "Gasoline");

        dog1.animalSound(dog1.getDogName()); // Inherited
        dog1.animalWalk();  // Inherited
        dog1.animalEat();   // Inherited

        dog1.displayDetails(); // Custom method
    }
}
