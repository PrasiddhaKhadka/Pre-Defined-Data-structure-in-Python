// Abstract class
abstract class Animal {
    String name;

    // Constructor
    Animal(String name) {
        this.name = name;
    }

    // Abstract method (must be implemented by subclasses)
    abstract void sound();

    // Concrete method (can be directly used by subclasses)
    void eat() {
        System.out.println(name + " is eating...");
    }
}

// Subclass Dog
class Dog extends Animal {
    Dog(String name) {
        super(name);
    }

    @Override
    void sound() {
        System.out.println(name + " says: Woof! Woof!");
    }
}

// Subclass Cat
class Cat extends Animal {
    Cat(String name) {
        super(name);
    }

    @Override
    void sound() {
        System.out.println(name + " says: Meow! Meow!");
    }
}

// Main class
public class AbstractExample {
    public static void main(String[] args) {
        Animal dog = new Dog("Bruno");
        Animal cat = new Cat("Kitty");

        dog.sound(); // Woof! Woof!
        dog.eat();   // Bruno is eating...

        cat.sound(); // Meow! Meow!
        cat.eat();   // Kitty is eating...
    }
}
