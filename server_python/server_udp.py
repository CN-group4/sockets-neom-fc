import socket

HOST = '0.0.0.0'
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serverul Python (UDP) este pornit pe portul {PORT}...")
    print("Astept primul mesaj de la client...")

    while True:
        data, addr = s.recvfrom(1024)
        mesaj_primit = data.decode('utf-8').strip()

        print(f"Mesaj primit de la {addr}: {mesaj_primit}")

        if mesaj_primit.lower() == 'exit':
            print("Clientul a inchis chat-ul.")
            break

        raspuns = input("Tu (Server Python): ")
        s.sendto(raspuns.encode('utf-8'), addr)

        if raspuns.lower() == 'exit':
            break