import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws Exception {
        ServerSocket server = new ServerSocket(5000);
        int count = 1;
        while(true){
            System.out.println("Server waiting...");
            Socket socket = server.accept();
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));   
            System.out.println("Received: " + in.readLine() + " " + count);
            out.println("Hello From Server!");
            count += 1;
            socket.close();
        }
    }
}
