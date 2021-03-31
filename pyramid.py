blocks = int(input("Enter the number of blocks: "))

i=0
block=0
height=0
while block < blocks:
    i+=1
    block+=i
    if block < blocks:
        height+=1

    
    

print("The height of the pyramid:", block,"i",i,"height",height)
