s=list("#++++")
print("".join(s))
for i in range(0,len(s)-1):
    s[i],s[i+1]=s[i+1],s[i]
    print("".join(s))