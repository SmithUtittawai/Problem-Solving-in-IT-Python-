#6306021631061 สมิทธ์ อุทิศถวาย
import random
def Show():
    print("Select Option")
    print("1.Sex")
    print("2.Payment type")
    print("3.Education")
    print("4.Age group")


def Init():
    for r in range(55):
        data.append([0,0,0,0,0])
    for r in range(5):
        result.append([0,0,0,0,0])

def Enter():
    for r in range(55):
        for s in range(5):
            if s==0: #Sex (1-2)
                data[r][s]=random.randint(1,2)
            if s==1: #Payment type (1-3)
                data[r][s]=random.randint(1,3)
            if s==2: #Education (1-5)
                data[r][s]=random.randint(1,5)
            if s==3: #Age group
                data[r][s]=random.randint(1,80)
                if data[r][s]<21:
                    data[r][s]=1
                elif data[r][s]<40:
                    data[r][s]=2
                else:
                    data[r][s]=3
            data[r][s]-=1

def Choose():
    global option1,option2
    while(option1==option2):
        option1= -1
        while(option1<1 or option1>4):
            option1=int(input("Enter option 1[1-4] : "))
        option2= -1
        while(option2<1 or option2>4):
            option2=int(input("Enter option 2[1-4] : "))
        if option1--option2:
            print("Option1 & Option2 must unequal")
        
def Calc():
    global RMAX,CMAX
    for Q in range(55):
        R=data[Q][option1-1]
        C=data[Q][option2-1]
        result[R][C]+=1
        if R>RMAX: RMAX=R
        if C>CMAX: CMAX=C

def Print():
    global option1,option2
    if option1==1: string1="Sex"
    elif option1==2: string1="Payment type"
    elif option1==3: string1="Education"
    elif option1==4: string1="Age group"

    if option2==1: string2="Sex"
    elif option2==2: string2="Payment type"
    elif option2==3: string2="Education"
    elif option2==4: string2="Age group"


    print(f"\n Relationship between {string1} & {string2} \n")
    for r in range(5):
        for c in range(4):
            if result[r][c] !=0:
                print(result[r][c],end="\t")
        print()

#Main Program
data=[]
result=[]
option1=0
option2=0
RMAX=0
CMAX=0
print("Cross Tabulation \n\n".center(50))
Show()
Init()
Enter()
Choose()
Calc()
Print()
