with open("exam_log.txt" , "w") as log_file:
    log_file.write("User logged in.\n")

with open("exam_log.txt" , "a") as log_file:
    log_file.write("User logged out.\n")
