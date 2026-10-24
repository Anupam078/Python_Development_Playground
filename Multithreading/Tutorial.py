import threading
import time

def downloading_files():
    time.sleep(5)
background_thread=threading.Thread(target=downloading_files)
background_thread.start()
print("Main Thread still running...")