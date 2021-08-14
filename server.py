import socket
import threading
import os
import constant
import shutil


HEADER = 1024
PORT = 3000
server = socket.gethostbyname(socket.gethostname())
ADDR = (server, PORT)
FORMAT = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, PORT))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        comm = msg_length.split()
        command = comm[0]

        print(command)
        print(f'Received from { addr }')

        if command == constant.LIST_ALL:
            strfiles = ""
            for x in os.listdir(constant.PATH):
                strfiles += x+"\n"
            conn.send(strfiles[:-1].encode(FORMAT))

        elif command == constant.CREATE_BUCKET:
            new_bucket = constant.PATH + f'/{ comm[1] }'
            try:
                os.mkdir(new_bucket)
            except OSError:
                conn.send(bytes('[307] BUCKET ALREADY EXISTS', FORMAT))
            else:
                conn.send(bytes('[100] BUCKET CREATED', FORMAT))

        elif command == constant.DELETE_BUCKET:
            bucket = constant.PATH + f'/{ comm[1] }'
            try:
                os.rmdir(bucket)
            except OSError:
                conn.send(bytes('[304] BUCKET NOT FOUND', FORMAT))
            else:
                conn.send(bytes('[200] BUCKET DELETED', FORMAT))

        elif command == constant.LIST_BUCKETS:
            bucket1 = os.listdir(constant.PATH)
            bucketname = ""
            for buck in bucket1:
                if os.path.isdir(os.path.join(buck)):
                    bucketname += buck+"\n"
            conn.send(bucketname[:-1].encode(FORMAT))

        elif command == constant.LIST_FILES:
            files = os.listdir(constant.PATH)
            filesname = ""
            for file in files:
                if os.path.isfile(os.path.join(file)):
                    filesname += file+"\n"
            conn.send(filesname[:-1].encode(FORMAT))

        elif command == constant.UPLOAD_FILE:
            filename = comm[1]
            try:
               shutil.copy(filename, constant.PATH)
               conn.send("[400] FILE UPLOADED".encode(FORMAT))
            except:
                conn.send("[401] FAILED TO UPLOAD".encode(FORMAT))

        elif command == constant.DOWNLOAD_FILE:
            filename = comm[1]
            try:
                shutil.copy(filename,comm[2])
                conn.send("[402] FILE DOWNLOADED".encode(FORMAT))
            except:
                conn.send("[403] FAILED TO DOWNLOAD".encode(FORMAT))
        elif command == constant.DELETE_FILE:
            file = constant.PATH + f'/{ comm[1] }'
            try:
                os.remove(file)
            except OSError:
                conn.send(bytes(f'[305] FILE NOT FOUND', FORMAT))
            else:
                conn.send(bytes(f'[201] FILE DELETED', FORMAT))
        elif command == constant.TRAVEL_PATH:
            try:
                os.chdir(constant.PATH + comm[1])
                constant.PATH += comm[1]
                conn.send(f"DIRECTORY CHANGED".encode(FORMAT))
            except OSError:
                conn.send(f"Can't change the Current Working Directory".encode(FORMAT))
        elif command == constant.BACK:
            try:
                os.chdir("../")
                constant.PATH = os.getcwd() + "/"
                conn.send(f"You went back from directory".encode(FORMAT))
            except OSError:
                conn.send(f"Can't go back from directory".encode(FORMAT)) 
        elif command == constant.HELP:
            conn.send(f'ALL, CBUCKET, DBUCKET, LBUCKET, LBUCKET, LFILE, UPFILE, DWFILE, DWFILE, DFILE, EXIT, CD, BK'.encode(FORMAT))
        elif command == constant.DISCONNECT_COMMAND:
            print(f'[CLIENT DISCONNECTED] { addr } disconnected')
            conn.send(bytes(f'[600] DISCONNECTED', FORMAT))
            connected = False
        elif command == "a":
            conn.send(constant.PATH.encode(FORMAT))
        else:
            conn.send(bytes(f'[300] UNKNOWN COMMAND', FORMAT))

    conn.close()


def start():
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(10)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        constant.PATH = 'C:/Users/Santiago/Desktop/proyecto_Telematica/server_files/'


print(f"[STARTING] server is starting...")
start()
