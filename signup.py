import shelve
def signup():
    if __name__=="__main__":

        print("ARE YOU READY TO BECOME THE MEMBER OF MY BANK")
        name=input("Enter your name").lower().strip()
        passw=input("Enter your password:")
        balance=int(input("Enter your balance:"))
        db=shelve.open("dbdata\initial_details",writeback=True)
        acc=int(db['last_acc'])+1
        acc=str(acc)
        db['last_acc']=acc
        db['acc']={name:name,password:passw,balance:balance}
        print("YOU ARE SIGNED UP SUCCESFULLY!!")
        print("REMEMBER YOUR DETAILS--->{} {} {} ".format(db['acc']),db['acc']['name'],db['acc']['password'])
        db.close()
