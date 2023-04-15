from threading import Thread
from time import sleep
 
# function to create threads
def threaded_function(name, arg):
    for i in range(arg):
        print("running",i, name)
         
        # wait 1 sec in between each thread
        sleep(1)
 
 
if __name__ == "__main__":
    threadA = Thread(target = threaded_function, args = ("A",20, ))
    threadB = Thread(target = threaded_function, args = ("B",20, ))
    threadA.start()
    threadB.start()
    threadA.join()
    threadB.join()
    
    print("thread finished...exiting")