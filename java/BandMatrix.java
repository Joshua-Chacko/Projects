public class BandMatrix {
    public static void main(String[] args){
        int n = Integer.parseInt(args[0]);
        int width = Integer.parseInt(args[1]);

        String[][] matrix = new String[n][n];

        // Initialize the matrix with "0 "
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] = "0 ";
            }
        }

        // Fill the band around the diagonal
        for (int i = 0; i < n; i++) {
            for (int j = Math.max(0, i - width); j <= Math.min(n - 1, i + width); j++) {
                matrix[i][j] = "* ";
            }
        }

        // Print the matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrix[i][j]);
            }
            System.out.println();
        }
    }
}
