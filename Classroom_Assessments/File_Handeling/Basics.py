with open("exam_log.txt" , "w") as log_file:
    log_file.write("User logged in.\n")

with open("exam_log.txt" , "a") as log_file:
    log_file.write("User logged out.\n")

with open("server_log.txt","r") as read_log:
    log_list=read_log.readlines()

Error_log=[]
for line in log_list:
    words=line.split()
    for word in words:
        if "ERROR" in line:
            Error_log.append(line)

with open("error_logs.txt","w") as write_error:
    write_error.writelines(Error_log)
