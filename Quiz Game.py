import mysql.connector as sqltor
mycon = sqltor.connect(host="localhost", user="root", password="pass", database="quizdb")

# Function To Check if Set is Present
def check_Set(set_id):	
	sql ='select count(*) from qSet where sid='+set_id	
	c =mycon.cursor(buffered=True)
	c.execute(sql)
	result = c.fetchone()
	r = result[0]
	if (r >= 1):
	     return True
	else:
	     return False

# Function To Check Active Set is Present
def check_Active():	
	sql ="select count(*) from aSet"
	c =mycon.cursor(buffered=True)
	c.execute(sql)
	result = c.fetchone()
	r = result[0]
	if (r == 1):
	     return True
	else:
	     return False
	    
# Function To Check User 
def check_User(mob):	
	sql ="select count(*) from user where mob like '"+mob+"'"	
	c =mycon.cursor(buffered=True)
	c.execute(sql)
	result = c.fetchone()
	r = result[0]
	if (r >= 1):
	     return True
	else:
	     return False


# Function to Add_Set
def Add_Set():
        Id = input("Enter Set Id : ")
        if( check_Set(Id)== True ):
            print("Set already exists\nTry Again\n")            
        else:
            for i in range (1,3):
                qid=i;
                print("Question: ", i)
                ques = input("Enter Question:")
                ans1 = input("Enter Option 1:")
                ans2 = input("Enter Option 2:")
                ans3 = input("Enter Option 3:")
                ans4 = input("Enter Option 4:")
                cans = input("Enter correct option number:")
                c =mycon.cursor()
                c.execute("insert into qSet values(%s,%s,%s,%s,%s,%s,%s,%s)", (int(Id), int(qid), ques, ans1, ans2, ans3, ans4, int(cans)))
                mycon.commit()
                print("---------Question ADDED SUCCESSFULLY !--------- ")
        adminMenu()


# Function to Add_Set
def Add_Set():
        Id = input("Enter Set Id : ")
        if( check_Set(Id)== True ):
            print("Set already exists\nTry Again\n")            
        else:
            for i in range (1,3):
                qid=i;
                print("Question: ", i)
                ques = input("Enter Question:")
                ans1 = input("Enter Option 1:")
                ans2 = input("Enter Option 2:")
                ans3 = input("Enter Option 3:")
                ans4 = input("Enter Option 4:")
                cans = input("Enter correct option number:")
                c =mycon.cursor()
                c.execute("insert into qSet values(%s,%s,%s,%s,%s,%s,%s,%s)", (int(Id), int(qid), ques, ans1, ans2, ans3, ans4, int(cans)))
                mycon.commit()
                print("---------Question ADDED SUCCESSFULLY !--------- ")
        adminMenu()

# Function to Add_Set
def new_Contestent():
        mob = input("Enter Mobile No : ")
        uname = input("Enter Name : ")
        if(check_User(mob)== True ):
            print("User Already Exist\n\n")
            
        else:
            c =mycon.cursor()
            c.execute("insert into user values(%s,%s)", (mob,uname))
            mycon.commit()
            print("------------------------ User Created--------------------")        
            
        constMenu()

def adminMenu():
        p=input("Enter your Pass Key ")
        if p=='rajarshi':
            print("~WELCOME TO Admin Console ~~~~~~~~~")
            print("Press")
            print("1.Add Set")
            print("2.Active Set")	
            print("3.Exit")
            ch = int(input("Enter your Choice "))
            if ch == 1:
                Add_Set()		
            elif ch == 2:
                Active_Set()			
            elif ch == 3:
                exit(0)		
            else:
                print("INVALID CHOICE!!!!!")
        else:
            print("INVALID PassKey!!!!!")
            menu()

def play():
    mob = input("Enter Mobile No : ")
    if(check_User(mob)== False ):
        print("Please Create your Account\n\n")
    else:
        sql ='select sid  from aSet'
        c =mycon.cursor(buffered=True)
        c.execute(sql)
        result = c.fetchone()
        aset = result[0]        
        sql="select * from qSet where sid="+str(aset)
        c =mycon.cursor()
        c.execute(sql)
        r = c.fetchall()
        
        score=0
        for x in r:
            print(x[1],x[2])
            print("1.", x[3],"2.", x[4], "3.", x[5],"4.",x[6])
            a=int(input("Enter your ans. "))
            if(a==x[7]):
                  print("Correct")
                  score=score+1
            else:
                  print("Woops..")
    print("Your score is",score)
	
	

def constMenu():
    print("~WELCOME TO Contestent Console ~~~~~~~~~")
    print("Press")
    print("1.Existing Contestent")
    print("2.New Contestent")
    print("3.Previous Menu")
    print("4.Exit")
    ch = int(input("Enter your Choice "))
    if ch == 1:
        play()		
    elif ch == 2:
        new_Contestent()			
    elif ch == 3:
        menu()
    elif ch == 4:
        exit(0)		
    else:
        print("INVALID CHOICE!!!!!")

def menu():
	print("~WELCOME TO QUIZ ~~~~~~~~~")
	print("Press")
	print("1.Contestent")
	print("2.Admin ")	
	print("3.Exit")
	ch = int(input("Enter your Choice "))
	if ch == 1:
		constMenu()		
	elif ch == 2:
		adminMenu()			
	elif ch == 3:
		exit(0)		
	else:
		print("INVALID CHOICE!!!!!")

menu()