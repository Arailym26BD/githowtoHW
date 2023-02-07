a = int(input())
b= []
while a != 0:
    a.append(x)
    a = int(input())
    
M = sum(a)/len(a)
STD = 0
for i in a:
    STD += (i-M)**2
STD = ( STD/(len(a)-1) )**0.5
print(STD)