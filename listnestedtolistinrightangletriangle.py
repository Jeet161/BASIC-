a=[10,[20,30],40,[50,60],70,[80]]
flat=[]
for item in a:
    if type (item)== list:
        for num in item:
            flat.append(num)
    else:
        flat.append(item)
    print("flatted list:",flat)
