#6306021631061 สมิทธ์ อุทิศถวาย
import random
def Show():
    print("Select Option")
    print("1.Age")
    print("2.Study At")
    print("3.Question: A")
    print("4.Question: B")
    print("5.Question: C")

def Init():
    for r in range(150):
        data.append([0,0,0,0,0])
    for r in range(5):
        result.append([0,0,0,0,0])

def Enter():
    for r in range(150):
        for s in range(5):
            if s==0: #Age (1-3)
                data[r][s]=random.randint(1,80)
                if data[r][s]<21:
                    data[r][s]=1
                elif data[r][s]<40:
                    data[r][s]=2
                else:
                    data[r][s]=3
            if s==1: #Study at (1-5)
                data[r][s]=random.randint(1,5)
            if s==2 or s==3 or s==4: #Yes/No
                data[r][s]=random.randint(1,2)
            data[r][s]-=1

def Choose():
    global option1,option2
    while(option1==option2):
        option1= -1
        while(option1<1 or option1>5):
            option1=int(input("Enter option 1[1-5] : "))
        option2= -1
        while(option2<1 or option2>5):
            option2=int(input("Enter option 2[1-5] : "))
        if option1--option2:
            print("Option1 & Option2 must unequal")
        
def Calc():
    global RMAX,CMAX
    for Q in range(150):
        R=data[Q][option1-1]
        C=data[Q][option2-1]
        result[R][C]+=1
        if R>RMAX: RMAX=R
        if C>CMAX: CMAX=C

def Print():
    global option1,option2
    if option1==1: string1="Age"
    elif option1==2: string1="Study At"
    elif option1==3: string1="Question ; A"
    elif option1==4: string1="Question ; B"
    elif option1==5: string1="Question ; C"

    if option2==1: string2="Age"
    elif option2==2: string2="Study At"
    elif option2==3: string2="Question ; A"
    elif option2==4: string2="Question ; B"
    elif option2==5: string2="Question ; C"

    print(f"\n Relationship between {string1} & {string2} \n")
    for r in range(5):
        for c in range(5):
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
    
    
