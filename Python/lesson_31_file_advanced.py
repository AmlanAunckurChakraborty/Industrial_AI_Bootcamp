#Professional way of handling file, so colse() needed
print("\n======Professinal way======")

with open("data.txt", "w") as file: #write here as file means file is a veriable which stores the file data
    file.write("Hello Amlan\n")
with open("data.txt", "a") as file: #appand
    file.write("New writting added Amlan\n new line 3\n new line 4\n new line 5\n")
with open("data.txt", "r") as file: # read
    file.read()

#read()
with open("data.txt", "r") as file:
    data = file.read(11)                   #read entite file
print(data) #print can be done inside or outfile file as file readed and stored in memory

# readline()

# Unlike read(), readline() reads only one line at a time.
# Each time readline() is called, it reads the next line in the file.
# The optional number inside readline(n) specifies the maximum number of
# characters to read from that line, NOT the number of lines.

with open("data.txt", "r") as file:
    data1 = file.readline(5)   # Reads up to 5 characters from the first line
    data2 = file.readline(5)   # Reads the next 5 characters (or continues according to file position)
    data3 = file.readline(5)   # Reads the next 5 characters

    print(data1, data2, data3)

# print(file.readline(2), file.readline(2), file.readline(2), file.readline(3))
# This actually works if it is inside the 'with' block.
# Each readline() call continues reading from the current file position.

# print(file.readline(1), file.readline(2), file.readline(3), file.readline(4))
# This will NOT work outside the 'with' block because the file is automatically closed.

#readlines it can read all the lines
file = open("data.txt","r")
data = file.readlines()
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
file.close()

file = open("data.txt","r")
data = file.readlines(4)  # readlines(4) does NOT read the first 4 lines.The number (4) specifies the approximate number of BYTES (or characters)m,to read, not the number of lines.Since readlines() always returns complete lines, it usually returns,the first line if its size reaches or exceeds the requested value.
# so this is invalid
print(data)
file.close()

#smart thing 
with open("data.txt", "r") as file:
    data = file.readlines()
#We can simple call the whole read in a list of strings then can use them anywhere in the program , all the lines will be called during calling the file
#with loop
with open("data.txt","r") as file:
 values = file.readlines()
 for value in values:
    print(value)

#write()
#mobile ditectory
print("\n=== Final Ones Data set ===\n")
import random as r

operator_identifier = ["7","3","9","4","8","6","5"]
user_ratio = [40,15,20,8,10,5,2]

with open("mobile directory.txt", "a") as file:
    file.write("\n==== New Data Set Has Arrived ====\n")
    for _ in range(30):
        third_digit = r.choices(operator_identifier,
                                weights=user_ratio,
                                k=1)[0]
        phone = "+880-1" + third_digit + str(r.randint(10000000,99999999))
        file.write(phone + "\n")

#tell
with open("data.txt", "r") as file:
    print(file.tell()) # so it tells us  file pointer is at its initial position 0 as list of string starts with 0
    file.read(5)
    print(file.tell())
    file.read(3)
    print(file.tell())
    file.read(1)
    print(file.tell()) # so it tells us where the file pointer is its now at line 9 cause 5+3+1=9

  #seek moves the pointer position

    with open("data.txt","r") as file:
     print(file.read(5))
     file.seek(0)
     print(file.read(5))
     file.seek(3)
     print(file.read(5)) # file tell also go the position and tells only the pointer but seek move the potiner so can get the string values of the position it moves by cherecter not by line

#r+,a+,w+
#r+ read and write everything file only file exists, file must exits
#w+ write and read , but if file exists it will override and replace the initial text
#a+ read and write but write at the end so it is maybe the most useful writing tool