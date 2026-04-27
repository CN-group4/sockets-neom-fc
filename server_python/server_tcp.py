import socket

HOST = '0.0.0.0' 
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Serverul Python (TCP) asteapta conexiuni pe portul {PORT}...")
    
    conn, addr = s.accept()
    with conn:
        print(f"Client Java conectat de la: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            mesaj_primit = data.decode('utf-8').strip() 
            
            if mesaj_primit.lower() == 'exit':
                print("Clientul Java a inchis conexiunea.")
                break
            
            print(f"Client (Java): {mesaj_primit}")
            
            raspuns = input("(Server Python): ")
            
            raspuns_cu_newline = raspuns + '\n' 
            conn.sendall(raspuns_cu_newline.encode('utf-8'))
            
            if raspuns.lower() == 'exit':
                break