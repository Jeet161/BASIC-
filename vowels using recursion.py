def vowels(s):
    if not s:
        return 0
    if s[0].lower()in "aeiou":
        return 1 + vowels(s[1:])
    else:
        return vowels(s[1:])
text= input("Enter a string:")
print("Number of vowels:", vowels(text))  
       
    