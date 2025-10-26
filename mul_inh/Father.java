public class Father extends GrandFather{

    String profession;

    Father(String familyname, String profession){
        super(familyname);
        this.profession = profession;
    }
    
    void showProfession(){
        System.out.println("Profession: " + profession);
    }
}