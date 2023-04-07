import mysql.connector
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="lms"
)


mycursor = mydb.cursor()


z="""
!!!!!!!!!!!!!!!!!Invalid Input. Try again!!!!!!!!!!!!!!!!!!!!
"""
#AN   === available or not
#BN   === book name
#FARD === fantasy, action, romance, Drama
#BNO  === booknumber

def choosegenre():
    while True:
        print("""
                    Choose Genre
                    1. Fiction
                    2. Action
                    3. Romance
                    4. Drama 
        """)
        i = input("=>")
        if i.isnumeric():
            i = int(i)
            if i == 1:
                return "f"
            elif i == 2:
                return "a"
            elif i == 3:
                return "r"
            elif i == 4:
                return "d"
            else:
                print("Invalid Input.... Choose a Proper Option")
        elif i.lower() == "home()":
            return None
        elif i.lower() == "back()":
            print(i)
            return "back"
        else:
            print(z)


def choosebook(g,ad):
    if g==None:
        return
    elif g=="back":
        return
    if ad=="D":
        mycursor.execute(f"select bno,bn from books where fard='{g}'")
        books=mycursor.fetchall()
    else:
        mycursor.execute(f"select bno,bn from books where fard='{g}' and AN='A'")
        books=mycursor.fetchall()
    a=0
    for i in books:
        print((f"{a+1}. {i[-1]}").center(55))
        a+=1
    while True:
        key = input("=>")
        if key.isnumeric():
            key = int(key)
            if key > 0 and key <= len(books):
                bookno = books[key-1]
                return bookno[0]
            else:
                print("Invalid Input Try again")
        elif key.lower() == 'home()':
            return
        elif key.lower() == 'back()':
            return "back"
        else:
            print("Invalid Input Try again")

def bookchoose(AD):
    while True:
        x=choosebook(choosegenre(),AD)
        if x==None:
            return
        elif x=="back":
            continue
        else:
            return x

def registrationnumber():
    while True:
        key=input("Registration Number: ")
        if key.isnumeric():
            key=int(key)
            mycursor.execute(f"select * from members where rno={key}")
            x=mycursor.fetchall()
            if len(x):
                return x[0][0]
            else:
                print("Member Not Found")
        elif key.lower()=="back()":
            return "back"
        elif key.lower()=="home()":
            return None
        else:
            print(z)
    
def booknumber():
    while True:
        key=input("Enter the Book Number =")
        if key.isnumeric():
            key=int(key)
            mycursor.execute(f"select * from books where bno={key}")
            x=mycursor.fetchall()
            if len(x):
                return x[0][0]
            else:
                print("Book Not found Try again")
        elif key.lower()=="back()":
            return("back")
        elif key.lower()=="home()":
            return None
        else:
            print(z)

def already(y):
    mycursor.execute(f"select * from books where an='{y}'")
    if mycursor.fetchall()==[]:
        return False
    else:
        return True

def issuebook():
    while True:
        x=bookchoose("A")
        if x==None:
            return
        else:
            while True:
                y=registrationnumber()
                if y=="back":
                    break
                elif y==None:
                    return 
                elif type(y)==int:
                    if already(y):
                        print("               A person can have only one book. ")
                        print("The Member already have a book. Return The book To get a New Book")
                        return
                    else:
                        mycursor.execute(f"update books set an='{y}' where bno={x}")
                        mycursor.execute(f"update members set bis={x}")
                        mydb.commit()
                        print()
                        print("::::::::::::::::::::  BOOK IS ISSUED ::::::::::::::::::::")
                    break
            break
    

def returnbook():
    while True:
        x=registrationnumber()
        if x==None :
            return
        elif x=="back":
            break
        else:
            if already(x):
                while True:
                    mycursor.execute(f"select bno,bn from books where an='{x}'")
                    t=mycursor.fetchall()
                    print()
                    i = input(f"Enter 'subimt' to submit the {t[0][-1]} =>")
                    if i.lower()=="submit":
                        mycursor.execute(f"update books set an='A' where bno={t[0][0]}")
                        mycursor.execute(f"update members set bis={x}")
                        mydb.commit()
                        
                        print("""
::::::::::::::::::::  BOOK IS SUBMITED ::::::::::::::::::::
                        """)
                        return
                    elif i.lower() == "back()":
                        break
                    elif i.lower() == "home()":
                        return
                    else:
                        print(z)
            else:
                print("You have not taken any book")
                return

def name(k):
    while True:
        Name = input(f'{k}: ').upper()
        if Name != 'HOME()':
            if len(Name) <= 25:
                return Name
            elif len(Name) >= 25:
                print('The character Exits 25 !!TRY AGAIN!!')
            else:
                print('Invalid Name !!TRY AGAIN!!')
        elif Name != 'BACK()':
            return"back"
        else:
            print('Invalid Name !!TRY AGAIN!!')

def mobno(noro):
    while True:
        no = input(f'{noro}: ')
        if no != 'HOME()':
            if no.isnumeric():
                c = len(no)
                if c == 10:
                    no = int(no)
                    return no
                else:
                    print('Number is less or more than 10 !!TRY AGAIN!!')
            else:
                print("Invalid Input Try again")
        elif no.upper() != 'BACK()':
            return"back"
        else:
            print('Invalid Number !!TRY AGAIN!!')
        

def address():
    while True:
        addr=input('Enter the Address(150char):')
        if addr.lower()!="home()":
            if len(addr)<=150 and len(addr)>0:
                return addr
            elif len(addr)>150:
                print('characters more than 150')
            elif addr != 'BACK()':
                return "back"
            else:
                print('Invalid input')
        else:
            return

def bookname():
    i=input("Book Name =>")
    if i=="":
        print(z)
        return None
    elif i.lower()=="back()":
        return "back"
    elif i.lower()=="home()":
        return
    else:
        return i


def addbook():
    while True:
        i=bookname()
        if i==None:
            return
        elif i=="back":
            break
        elif i!=None:
            while True:
                j=choosegenre()
                if j=='back':
                    break
                elif j != None:
                    mycursor.execute("select bno from books")
                    k=mycursor.fetchall()[-1][0]+1
                    print(k,j,i)
                    z="insert into books values({},'{}','{}','A')".format(k,i,j)
                    mycursor.execute(z)
                    print(f"Book Successfully Added and the Book Number is {k}")
                    mydb.commit()
                    return
                elif j==None:
                    return
                else:
                    break

def addmember():
    while True:
        a=random.randint(100,1000)
        mycursor.execute(f"select rno from members where rno={a}")
        o=mycursor.fetchall()
        if o==[]:
            break
        else:
            continue
    while True:
        print(f"Your registration Number will be {a}")
        i=name("Name")
        if i==None or i == 'back':
            return
        else:
            while True:
                j=mobno("Phone")
                if  j==None:
                    return
                elif j=='back':
                    break
                else:
                    while True:
                        k=address()  
                        if k==None:
                            return
                        elif k=="back()":
                            break
                        else:
                            mycursor.execute(f"insert into members values ({a},'{i}',{j},'{k}',0)")
                            mydb.commit()
                            print(f"Member {i} added sucessfully")
                            print(f"The registration number is {a}")
                            return

def seemembers():
    mycursor.execute("select*from members")
    i=mycursor.fetchall()
    if i!=[]:
        if i[-1]==0:
            for x in i:
                print(f"[{x[0]}] {x[1]} ||| No Books taken||| {x[2]} ||| {x[3]}")
        else:
            for x in i:
                print(f"[{x[0]}] {x[1]} ||| Book Taken:{x[-1]} ||| {x[2]} ||| {x[3]}")
    else:
        print("No Members are registered")

def main():
    while True:
        print("""
        1. Issue Book
        2. Return Book
        3. Add Book
        4. Add Member
        5. See members
        Enter exit() to Exit
        """)
        i = input("=>")
        if i.isnumeric():
            i = int(i)
            if i == 1:
                issuebook()
            elif i == 2:
                returnbook()
            elif i == 3:
                addbook()
            elif i == 4:
                addmember()
            elif  i==5:
                seemembers()
            else:
                print("Invalid Input.... Choose a Proper Option")
        elif i.lower() == "exit()":
            return
        else:
            print("Invalid Input.... Choose a Proper Option")


main()
