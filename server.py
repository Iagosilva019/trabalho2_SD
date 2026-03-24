import socket
import threading
from datetime import datetime

HOST = '0.0.0.0'
PORT = 50007


def arquivo(log):
    with open("log.txt","a") as arq:
        arq.write(log + "\n")

    
def data_hora():
    agora = datetime.now()

    # Formatar data e hora (Ex: 24/03/2026 15:30:00)
    formato = agora.strftime("%d/%m/%Y %H:%M:%S")
    #print("Data e Hora Formatada:", formato)
    return formato

def handle_client(conn, addr):
    print("Conectado:", addr)

    try:
        
        data = conn.recv(1024)
        if not data:
            print("Cliente desconectou:", addr)
           
           

        print(f"{data_hora()}:{addr} ->", data.decode())
        arquivo(f"{data_hora()}:{addr} -> {data.decode()}")
        conn.sendall(b"ok")

    except ConnectionResetError:
        print("Cliente fechou conexão à força:", addr)

    finally:
        conn.close()


            

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Aguardando dados dos sensores... {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()