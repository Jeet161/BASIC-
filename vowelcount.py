a= input("enter a words")
vowel=set("aeiouAEIOU")
count=0
for chr in a:
    if chr in vowel:
        count+=1
print(count)        