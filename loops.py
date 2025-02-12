#loops in python

#for loop without conditions
for i in range(0,10):
    '''print(i)'''
    
#for loop with conditions
for i in range(0,10,2):
    print(i)
    
#while loop without conditions
while(True):
    print("WHILE LOOP")
    break

#while loop with conditions
j=0
while(j<=10):
    print(j)
    j=j+1

#match case
print("1. FOR HELLO")
print("2. FOR WELCOME")
ch=int(input("Enter your choice"))
match ch:
    case 1:
            print("hello")
    case 2:
            print("Welcome")
            
 #OR FOR CASE
            
#Using if elif else

print("1. FOR HELLO")
print("2. FOR WELCOME")
ch=int(input("Enter your choice"))
if(ch==1):
     print("hello")
elif(ch==2):
     print("Welcome")
else:
    print("Invaild Choice")
