interface A{
    void m1();
    void m2();
    void m3();

    
    // AFTER JAVA 8

    // default void m4(){
    //     System.out.println("m4");
    // }
}


class B implements A{
    public void m1(){
        System.out.println("m1");
    }
    public void m2(){
        System.out.println("m2");
    }
}

public class Inter {
    public static void main(String[] args) {
        B obj = new B();
        obj.m1();
        obj.m2();
        // obj.m3();
    }
}
