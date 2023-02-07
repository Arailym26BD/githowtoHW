s=input()
rn=len(s)
for i in range(rn):
    if i%3==0:
        s=s.replace(s[i], '3', 1)
print(s.replace('3', ''))