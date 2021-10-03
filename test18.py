#Health management system



#3 client - harry Rohan and hammad
#total 6 File
#Write an function when exected takes as input client name 
#
#def getdate():
#    inport datetime
#    return datetime.datetime.now()

#one more functon to retrive exercise or food of the client

def getdate():
    import datetime
    return datetime.datetime.now()
print("Enter your client detail")
print("1 for Harry\n 2 for Rohan\n 3 for Hammad")
n=int(input())
if n==1:
    print("Data is about food or gym")
    print("1 for data\n2 for gym")
    m=int(input())
    if(m==1):
        f=open("Harryfood.txt","a")
        print("Enter what he eat")
        s=input()
        f.write(s)
        f.write("\n")
        f.write(str(getdate()))
        f.write("\n")
        f.close
    elif(m==2):
        f=open("Harrygym.txt","a")
        print("Enter what exercise he does")
        s=input()
        f.write(s)
        f.write("\n")
        f.write(str(getdate()))
        f.write("\n")
        f.close
    else:
        print("You select wrong option please select correct option")
elif n==2:
    print("Data is about food or gym")
    print("1 for data\n2 for gym")
    m=int(input())
    if(m==1):
        f=open("Rohanfood.txt","a")
        print("Enter what he eat")
        s=input()
        f.write(s)
        f.write("\n")
        f.write(str(getdate()))
        f.write("\n")
        f.close
    elif(m==2):
        f=open("Rohangym.txt","a")
        print("Enter what exercise he does")
        s=input()
        f.write(s)
        f.write("\n")
        f.write(str(getdate()))
        f.write("\n")
        f.close
    else:
        print("You select wrong option please select correct option")
elif n==3:
    print("Data is about food or gym")
    print("1 for data\n2 for gym")
    m=int(input())
    if(m==1):
        f=open("Hammadfood.txt","a")
        print("Enter what he eat")
        s=input()
        f.write(s)
        f.write("\n")
        f.write(str(getdate()))
        f.write("\n")
        f.close
    elif(m==2):
        f=open("Hammadgym.txt","a")
        print("Enter what exercise he does")
        s=input()
        f.write(s)
        f.write("\n")
        f.write(str(getdate()))
        f.write("\n")
        f.close
    else:
        print("You select wrong option please select correct option")
else:
    print("You select wrong option please select correct option")