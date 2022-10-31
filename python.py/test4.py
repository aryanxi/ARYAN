M=[]

def matrix():
    print("Matrix is accept here")
    print("Enter the no of rows :")
    r=int(input())
    print("ENter the columns :")
    c=int(input())

    for i in range(r):
        a=[]
        for j in range(c):
            x=input()
            a.append(x)
        M.append(a)
            
    for i in range(r):
        for j in range(c):
            print(M[i][j],end=" ")
        print("\n")
matrix()



def table():
    i=1;
    num=int(input("enter the no :"))
    for i in range(1,11):
        x=num*i
        print("%d X %d = %d"%(num,i,x);


def design()
    rows=10
    i,j=0,0
    for i in range(0,rows):
        print()
        for j in range(0,i+1):
            print("0",end=" ")



def sign():
    rows=10
    col=10
    i,j=0,10
    for i in range(0,rows):
        print("0",end=" ")
        for j in range(col,j-1):
            print()




sign()

def s():
    x=str(input("Enter the pallidrome program :"))

    y= x [:: -1]
    if(x==y):
        print("The given function is pallidrome")
    else:
        print("The function is not pallidrome")

    

s()