
class drone {
    int energy;
    int highest;
    int speed;
    String brand;

    void fly(){
        energy--;
        if(energy > 5){
            highest++;
            System.out.println("The Drone is flying!! ");
        }else{
            System.out.println("Danger: Low energy, the drone can't fly anymore!");
        }
        }
        void turnOff(){
            if(highest > 0){
                System.out.println("Machine can't to turn off, because it's about fly");
            } else{
                System.out.println("Machine turn off");
            }
        }
    
        void down(){
            highest--;
            energy--;
            System.out.println("The Drone is down...");
        }
        void trun(){
            energy--;
            System.out.println("The Drone is turn");
        }
        void forward(){
            energy--;
            System.out.println("Drone being forward");
        }
        void backward(){
            energy--;
            System.out.println("Drone being backward");
        }
    }

