card=input("Enter the your credit card:")
total1=0
total2=0
x=len(card)+1
for i in range(-1,-x):
    if(i%2==0):
        total1+=int(card[i])*2
    else:
        total2+=int(card[i])
total3=total1+total2
if(total3%10!=0):
    print("Invalid")
else:
    test=card[0]+card[1]
    if(int(test)==34 or int(test)==37):
        print("American Express\n")
    elif(int(test)>=51 and int(test)<=55):
        print("Master card\n")
    elif(int(card[0])==4):
        print("Visa card\n")
    else:
        print("Invalid")



