interface CanRun {
    void run();
}

interface CanBark {
    // # can have abstract method and normal methods both
    // # but will have atleast one abstract method
    void run();

    // tv remote and tv
    // keyboard and mouse
}

class Dog implements CanRun, CanBark {
    public void run() { System.out.println("Dog runs"); }
    // public void bark() { System.out.println("Dog barks"); }
}

class Main {
    public static void main(String[] args) {
        Dog d = new Dog();
        d.run();
        // d.bark();
    }
}
