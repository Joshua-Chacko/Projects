public class GeneralizedHarmonicJava
{
    public static void main(String[] args) {
        int n = Integer.parseInt(args[0]);
        int r = Integer.parseInt(args[1]);
        float gen_Harm_Total = 0;

        int i = 1;
        while(n >= i){
            gen_Harm_Total += (1/Math.pow(i,r));
            i++;
        }
        System.out.println(gen_Harm_Total);
    }
}
