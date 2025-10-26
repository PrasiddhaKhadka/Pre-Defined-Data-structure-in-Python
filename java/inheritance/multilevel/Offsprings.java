public class Offsprings extends Father{

    String hobby;
    String newProfession;

    Offsprings(String familyname, String profession,String hobby, String newProfession){
        super(familyname, profession);
        this.hobby = hobby;
        this.newProfession = newProfession;
    }

    void showHobby() {
        System.out.println("Offspring's Hobby: " + hobby);
    }

    @Override
    void showProfession() {
        super.showProfession();
        System.out.println("New Profession: "+ newProfession );
    }

}


class Test{
    public static void main(String[] args) {
        Offsprings off1 = new Offsprings("Dhital", "Engineer", "Coding", "Designer");
        off1.showFamilyName();
        off1.showProfession();
        off1.showHobby();
    }
}