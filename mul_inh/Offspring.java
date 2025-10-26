public class Offspring extends Father{
 
    String hobby;
    String updatedProfession;

    Offspring(String familyname, String profession, String hobby,String updatedProfession){
        super(familyname, profession);
        this.hobby = hobby;
        this.updatedProfession = updatedProfession;
    }


// # Method overloading
    int Salary(int amount){
        // System.out.println("Salary: " + amount);
        return amount;
    }

    int Salary(int amount, int bonus){
        // System.out.println("Salary: " + (amount + bonus));
        return amount + bonus;
    }


// # method overiding
    void showProfession(){
        super.showProfession();
        System.out.println("Profession: " + updatedProfession);
    }

    void showHobby(){
        System.out.println("Offspring's Hobby: " + hobby);
    }
}


class Testing{
    public static void main(String[] args) {
        Offspring off1 = new Offspring("Dhital", "Engineer", "Coding","Doctor");
        off1.displaYFamilyName();
        off1.showProfession();
        off1.showHobby();
        System.out.println(off1.Salary(10000));
        System.out.println(off1.Salary(10000,2000));

    }
}