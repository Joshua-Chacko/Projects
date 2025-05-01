public class RandomWalker {
    public static void main(String[] args){
        int r = Integer.parseInt(args[0]);
        int y = 0 , x = 0;
        int Manhattan_Distance = Math.abs(x) + Math.abs(y);
        int steps = 0;
        System.out.println("(" + x +"," + y + ")");
        while (true) {
            if (Manhattan_Distance == r){
                break;
            }
            double rand = Math.random(); // Generates a value in [0.0, 1.0)
            if (rand < 0.25)         y++;       // North
            else if (rand < 0.50)    y--;       // South
            else if (rand < 0.75)    x++;       // East
            else                     x--;       // West
            System.out.println("(" + x +"," + y + ")");
            steps ++;
            Manhattan_Distance = Math.abs(x) + Math.abs(y);
        }
        System.out.println("Steps = "+ steps);
    }
}
