
public class game {
    public static void main(String[] args) {
        player noir = new player();

        noir.name = "Hendra";
        noir.speed = 50;
        noir.healthPoin = 10;

        noir.run();
        if(noir.isDead()){
            System.out.println("Game over!");
        }else{
            System.out.println("Dia kabur!");
        }
    }
}
