def length(s,d,l):
    if (d==s):
        return l
    else:
        d = s[:l+1]
        return length(s,d,l+1)

value = input("Enter the string : ")
k = length(value,"",0)
print(k) 