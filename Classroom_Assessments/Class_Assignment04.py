'''import csv
import pickle
import os

def calc_marks () :
  try :
    with open ('students.csv','r') as f_in, open ('processed_results.txt','w') as f_out, open ('error_log.txt','w') as f_err :
      lines = f_in.readlines()
      c = 1
      for l in lines :
        p = l.strip().split(',')
        if len (p) < 5 :
          f_err.write("line " + str(c) + " missing data\n")
          c = c + 1
          continue
        
        r = p[0]
        n = p[1]
        try :
          m1 = int (p[2])
          m2 = int (p[3])
          m3 = int (p[4])
          tot = m1 + m2 + m3
          f_out.write(r + " " + n + ": " + str(tot) + "\n")
        except ValueError :
          f_err.write("line " + str(c) + " invalid marks\n")
        
        c = c + 1
        
  except FileNotFoundError :
    print ("file missing")
  except PermissionError :
    print ("permission error")

class Student :
  def __init__ (self, r, n, m) :
    self.roll = r
    self.name = n
    self.marks = m

def fix_prog () :
  st = [ Student(101,"Ravi",80), Student(102,"Asha",92), Student(103,"Meena",75) ]
  with open ("students.dat", "wb") as f :
    for s in st :
      pickle.dump (s, f)
      
  with open ("students.dat", "rb") as f :
    while True :
      try :
        s = pickle.load (f)
        print (s.name, s.marks)
      except EOFError :
        break

def find_st (r_num) :
  try :
    with open ("students.dat", "rb") as f :
      while True :
        try :
          s = pickle.load (f)
          if s.roll == r_num :
            return s.name
        except EOFError :
          break
  except Exception :
    pass
  return "not found"

def pipe_ex () :
  rd, wr = os.pipe ()
  os.write (wr, b"Meena Asha Ravi")
  os.close (wr)
  
  d = os.read (rd, 100)
  print ("names from pipe = ", d.decode())
  os.close (rd)

calc_marks ()
fix_prog ()

found_name = find_st (102)
print ("search result 102 = ", found_name)

pipe_ex ()'''

# creating a dummy csv file so the code runs immediately and gives output
with open('students.csv', 'w') as f:
  f.write("101,Aarav,80,90,85\n")
  f.write("102,Neha,N/A,70,60\n")
  f.write("103,Rohan,75,85,95\n")
  f.write("104,Priya,90\n")

def calc_marks():
  try:
    with open('students.csv','r') as f_in, open('processed_results.txt','w') as f_out, open('error_log.txt','w') as f_err:
      lines = f_in.readlines()
      c = 1
      for l in lines:
        p = l.strip().split(',')
        if len(p) < 5:
          f_err.write("Line " + str(c) + " missing data\n")
          c = c + 1
          continue
        
        r = p[0]
        n = p[1]
        try:
          m1 = int(p[2])
          m2 = int(p[3])
          m3 = int(p[4])
          tot = m1 + m2 + m3
          f_out.write(r + " " + n + ": " + str(tot) + "\n")
        except ValueError:
          f_err.write("Line " + str(c) + " invalid marks\n")
        
        c = c + 1
        
  except FileNotFoundError:
    print("file missing")
  except PermissionError:
    print("permission error")

calc_marks()

# printing the contents of the files to the terminal for your screenshot
print("OUTPUT OF processed_results.txt :")
with open('processed_results.txt', 'r') as f1:
  print(f1.read())

print("OUTPUT OF error_log.txt :")
with open('error_log.txt', 'r') as f2:
  print(f2.read())