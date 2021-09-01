l=list(input().split())
p=[]
string="abcdefghijklmnopqrstuvwxyz"
for i in l:
    p.append(i.lower())


h="".join(p)
d=list(set(h))
d.sort()
s="".join(d)
print(s)
if string==s:
    print("Given string is anagram")
else:
    print("Given string is not anagram")

    


