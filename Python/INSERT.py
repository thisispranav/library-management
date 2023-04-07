import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="lms"
)

mycursor = mydb.cursor()

f=["Spells for Forgetting", "Kingdom of the Feared", "Killers of a Certain Age", "Foul Lady Fortune", "The Fortunes of Jaded Women", "The Marriage Portrait", "Thistlefoot", "The Family Game", "The Golden Enclaves", "Drunk on Love", "Lucy by the Sea", "The Ways We Hide", "House of Hunger", "The Sunbearer Trials", "A Merry Little Meet Cute"]
a=["The Killing Code", "Rust in the Root", "It Looks Like Us", "The Getaway", "Blood of Troy", "From the Shadows", "Peace Maker", "The Demon Code", "Robin, Vol. 1: Reborn", "Robin, Vol. 2: I Am Robin", "Cipher", "Vision of Virtue", "How to Date a Superhero", "Number One Fan", "Firestorm"]
r=["The American Roommate Experiment", "Spells for Forgetting", "Kingdom of the Feared", "Foul Lady Fortune", "When in Rome", "Dreamland", "The Golden Enclaves", "The Kiss Curse", "Angelika Frankenstein Makes Her Match", "Drunk on Love", "Defend the Dawn", "The Make-Up Test", "A Merry Little Meet Cute", "Lizzie Blake's Best Mistake", "The Matchmaker's Gift"]
d=["Reminders of Him", "Regretting You", "All Your Perfects", "Bone Deep", "Malibu Rising", "The Perfect Son", "The Paper Palace", "Evidence of the Affair", "Rich Blood", "Heart Bones", "Without Merit", "Apples Never Fall", "The Winners", "From the Embers", "Wish You Were Here"]
q=0
x=[f,a,r,d]
y=['f','a','r','d']
n=0
for i in x:
    for j in i:
        mycursor.execute(f"""insert into books values({q+1},"{j}","{y[n]}",'A')""") 
        mydb.commit()
        q+=1
    n+=1



