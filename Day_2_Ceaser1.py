def encryption(a,key): 
    e=''
    for i in data:
        if i in l:
            index1=l.index(i)+key
            if(index1>=len(l)):
                index1-=len(l)
            e=e+l[index1]
        elif i in u:
            index1=u.index(i)+key
            if(index1>=len(u)):
                index1-=len(u)
            e=e+u[index1]
    return(e)

def decryption(a,key): 
    d=''
    for i in data:
        if i in l:
            index1=l.index(i)-key
            d=d+l[index1]
        elif i in u:
            index1=u.index(i)-key
            d=d+u[index1]
    return(d)
while(True):
 t=int(input("Enter 1 of encryption and 2 for decryption: "))
 l=list(chr(a) for a in range(ord('a'),ord('a')+26))
 u=list(chr(a) for a in range(ord('A'),ord('A')+26))
 key=2
 if t==1:
    data=input("Enter the data(only alphabet) which has to be encrypted: ")
    e=encryption(data,key)
    print("Encrypted data is: ",e)
    break;
 elif t==2:
    data=input("Enter the data which has to be decrypted: ")
    d=decryption(data,key)
    print("Decrypted data is: ",d)
    break;
 else:
    print("Please enter valid input")
    continue