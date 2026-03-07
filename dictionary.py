"""d1= {1:"keyboard",2:"mouse",3:"screen"}
d2={1:"water",2:"fire",3:"land",4:"sky"}
print (d1[2])
print(d2[3])

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Adding a new key-value pair
d["age"] = 18

# Updating an existing value
d[1] = "Python dict"

print(d)

d={1:'tree',2:'earth',3:'sky',4:'fire',5: 'space','age':18}
del d[1]
print(d)

w= d.pop(2)
print(w)

key, val = d.popitem()
print(f"key: {key}, Value: {val}")

d = {1: 'Geeks', 2: 'For', 3: 'phone','age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")"""
    
#nested dictionary

d={1:"first",2:"second",3:"third",4:"forth"}
d2={1:"youtube",2:"flipkart",3:{'a':"instagram",'b':"facebook",'c':"whatsapp"}}
print(d2[3])
print(d[4])
w=int(input("enter a number"))
if w==1:
    print(d)
elif w==2:
    print(d2)
else:
    print("choose between 1 and 2")