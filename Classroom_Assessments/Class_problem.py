Sentancce=input("Write the Sentence:")
words=Sentancce.split()
f=open("output.txt","w")
for word in words:
    if len(word)>4:
        f.write(word)

import pyodbc

try:
    connection = pyodbc.connect("DSN=CompanyDB")
    cursor = connection.cursor()

    employee_id = input("Enter employee id: ")

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Invalid employee ID. Please enter a number.")
        exit()

    query = "SELECT name, salary FROM employee WHERE id = ?"

    cursor.execute(query, (employee_id,))
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print("Name:", row.name)
            print("Salary:", row.salary)
    else:
        print("Employee not found.")

except pyodbc.Error as e:
    print("Database error:", e)

finally:
    if 'connection' in locals():
        connection.close()