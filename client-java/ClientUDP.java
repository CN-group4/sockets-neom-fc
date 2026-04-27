import java.net.*;
import java.util.Scanner;

public class ClientUDP {
    public static void main(String[] args) {
        // INLOCUIESTE CU IP-UL TAILSCALE AL SERVERULUI PYTHON
        String serverIP = "100.66.217.64";
        int port = 5001;

        try (DatagramSocket socket = new DatagramSocket();
             Scanner scanner = new Scanner(System.in)) {

            InetAddress address = InetAddress.getByName(serverIP);
            System.out.println("Client UDP Java pornit. Trimite un mesaj!");

            while (true) {
                // 1. Trimitere mesaj
                System.out.print("Tu (Client Java): ");
                String mesaj = scanner.nextLine();
                byte[] sendBuffer = mesaj.getBytes("UTF-8");

                DatagramPacket sendPacket = new DatagramPacket(sendBuffer, sendBuffer.length, address, port);
                socket.send(sendPacket);

                if (mesaj.equalsIgnoreCase("exit")) break;

                // 2. Primire raspuns
                byte[] receiveBuffer = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                socket.receive(receivePacket);

                String raspuns = new String(receivePacket.getData(), 0, receivePacket.getLength(), "UTF-8");
                System.out.println("Server (Python): " + raspuns);

                if (raspuns.trim().equalsIgnoreCase("exit")) break;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}