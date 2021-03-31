n ,m=map(int,input().split())
c = ".|."

#Top Con
for i in range(n//2):
    print((c*i).rjust((m-3)//2,"-")+c+(c*i).ljust((m-3)//2,"-") ) 

print("WELCOME".center(m,"-"))    

for i in range(n//2):
    print((c*(n//2-i-1)).rjust((m-3)//2,"-")+c+(c*(n//2-i-1)).ljust((m-3)//2,"-") ) 
