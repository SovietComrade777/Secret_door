s=input("Welcome Here \n Hey Stranger Enter your role..\n1)Member[M] \n2)Student[S] \n3)Teacher[T]\n:::--")
l=["saokals","lopamaook","udhisnij"]
o=open("C:\\Users\\DELL\\Desktop\\LAbka\\pswrd.txt","r")

for i in range(0,len(l)):
    l[i]=o.readline()
if(s=='M'):
    i=input("We need to Verify you,Enter a password:\n")
    for j in range(0,len(l)):
        if(i==l[j]):
            od=open("C:\\Users\\DELL\\Desktop\\LAbka\\member.txt",'r')
            kd=input("Say my name!")
            if(kd=="aksu"):
                print(od.read())
else:
    i=input("We need to Verify you,Enter a password:\n ")
    if(s=='T'):
        name=input('Say my name ?\n::')
        print("You entered the correct name")
        l=open("C:\\Users\\DELL\\Desktop\\LAbka\\teacher.txt","r")
        a=l.read()
        print(a)
    else:
        name=input('Say my name ?\n::')
        print("You entered the correct name")
        k=open("C:\\Users\\DELL\\Desktop\\LAbka\\std.txt")
        m=k.read()
        print(m)
        
        
