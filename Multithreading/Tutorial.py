import threading
import time

guest_list=[]
list_lock=threading.Lock()
def add_user(username):
    with list_lock:
        guest_list.append(username)

"""def downloading_files():
    time.sleep(5)
background_thread=threading.Thread(target=downloading_files)
background_thread.start()
print("Main Thread still running...")"""

