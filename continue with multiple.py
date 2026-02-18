"""n=int (input("enter first number:"))
for i in range(0,n):
  if i%3==0:
   continue  
  print(i,end="")
  
  #only multiple of 3
  n=int (input("enter first number:"))
for i in range(1,n+1):
 if i%3==0:
  print(i)
 else:
   continue
   

f = open("jeet.txt", "r")
print(f.read())

f = open("jeet.txt", "w")
print(f.write("krish"))"""

file = open("jeet.txt", "r")
content = file.read()
print(content)
file.close()
#write a file

with open("tame.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy with Python.")

print("File written successfully")

#with statement help to close
with open("jeet.txt", "r") as file:
    content = file.read()
    print(content)  