import threading
import time
import keyboard

stop_threads = False
show_state = 0

def run():
    while True:
        # print('thread running')
        time.sleep(0.01)
        if stop_threads:
            break
        if(show_state == 0):
            print("thread 0")
        else:
            print("thread 1")
 
def switch_x():
    global show_state
    if(show_state == 0):
        show_state = 1
    else:
        show_state = 0

# stop_threads = False
t1 = threading.Thread(target = run)
t1.daemon = True
t1.start()
# time.sleep(1)

while(True):
    if(keyboard.is_pressed('z')):
        stop_threads = True
        break
    keyboard.on_press_key('x', switch_x, suppress=False)
    # if(keyboard.is_pressed('x')):
        


t1.join()
print('thread killed')