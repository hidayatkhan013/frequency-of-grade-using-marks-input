count=[0,0,0,0,0]
while(True):
    score=float(input("Enter the next grade or (-1) to quit :"))
    if score>=90 and score<=100:
        count[0] +=1
    elif score>=80 and score<=89:
        count[1] +=1
    elif score>=70 and score<=79:
        count[2] +=1
    elif score>=60 and score<=69:
        count[3] +=1
    elif score>=0 and score<=59:
        count[4] +=1
    if score== -1:
        break

print("A :",count[0])
print("B :",count[1])
print("C :",count[2])
print("D :",count[3])
print("F :",count[4])