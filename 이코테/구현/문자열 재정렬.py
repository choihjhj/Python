s=input()
sum=0
s1=[]
for i in s:
    if i in '0123456789':
        sum+=int(i)
    else:
        s1.append(i)
if sum==0: sum=''
print(''.join(sorted(s1))+str(sum))        