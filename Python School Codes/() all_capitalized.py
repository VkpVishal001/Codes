def all_capitalized(s,d,i):
    if (i==len(s)):
        return d
    else:
        return all_capitalized(s,d+s[i].upper(),i+1)
    
w = input("Enter the word : ")
f = all_capitalized(w,"",0)
print(f)