# Task 01:

import sys
import subprocess

sys.stdout.write("System Helth Check...")

result=subprocess.run(["echo", "System Check Passed"],stdout=subprocess.PIPE,text=True)

with open("system_health.txt" , "a") as System_health_log:
    System_health_log.write(result.stdout)


# Task 02:
 
with open("records.txt","r+") as f:
    print(f.readline())
    f.seek(0,2)
    f.write("\n--- END OF RECORDS ---")
    f.read()
    print((int(f.tell())))
