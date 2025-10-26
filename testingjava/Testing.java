interface A{
    public void m1();
}
interface B{
    public void m1();

    default void m3(){
        System.out.println("m3");
    }

    static void m4(){
        System.out.println("m4");
    }


}


class Demo implements A,B{
    public void m1(){
        System.out.println("m1");
    }
    public void m2(){
        System.out.println("m2");
    }
    public static void main(String[] args) {
        Demo obj = new Demo();
        obj.m1();
        obj.m2();
        obj.m3();
        B.m4();
    }
}