s="y"
name=[]
roll=[]
count =0
while(s=="y"):
    name+=[raw_input("enter your name")]
    roll+=[raw_input("enter your roll no.")]
    s=raw_input("want to enter more ")
    count+=1
print"no. of data entered",
print count
if(s!="y"):
    i=0
    while(i<count):
        print(name[i])
        print ( roll[i])
        i=i+1
        
        print"\n"
