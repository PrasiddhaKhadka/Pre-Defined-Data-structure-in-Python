public class Poly {

    void display() {
        System.out.println("hello");
    }

    void display(int a) {
        for (int i = 0; i < a; i++) {
            System.out.println("hello");
        }
    }

    public static void main(String[] args) {
        Poly poly = new Poly();
        poly.display();
        poly.display(5);
    }
    
    }