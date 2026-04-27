import java.io.*;
import java.net.*;
import java.util.Scanner;

public class ClientTCP {
    public static void main(String[] args) {
        // INLOCUIESTE CU IP-UL TAILSCALE AL SERVERULUI PYTHON (ex: "100.x.x.x")
        String host = "100.66.217.64";
        int port = 5000;

        try (Socket socket = new Socket(host, port);
             Scanner scanner = new Scanner(System.in)) {

            System.out.println("Conectat la Serverul Python (TCP)!");

            // Folosim UTF-8
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream(), "UTF-8"));
            PrintWriter out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), "UTF-8"), true);

            while (true) {
                // 1. Trimitem mesajul catre Python
                System.out.print("Tu (Client Java): ");
                String mesaj = scanner.nextLine();

                out.println(mesaj); // 'println' adauga automat '\n' la final

                if (mesaj.trim().equalsIgnoreCase("exit")) {
                    break;
                }

                // 2. Asteptam raspunsul de la Python
                String raspuns = in.readLine(); // Asteapta pana primeste '\n'

                if (raspuns == null || raspuns.trim().equalsIgnoreCase("exit")) {
                    System.out.println("Serverul a inchis conexiunea.");
                    break;
                }

                System.out.println("Server (Python): " + raspuns);
            }
        } catch (IOException e) {
            System.out.println("Eroare de conectare: " + e.getMessage());
        }
    }
}