from getpass import getpass

import shelve
print("Please Fill Following Details")
def login():

     acc=input("Enter your name:")
     passw=getpass("Enter Your Password:")
     db=shelve.open("./initial_details")
     if acc in db['acc']and passw==db['acc']['password']:


         print("Successfully logged in .")
         s1='''
            1.Debit
            2.Credit
            3.Check balance
            4.Update password
            5.Submenu
            '''

         print(s1)
         
         ch2=int(input("Enter Your Choice:"))
         if ch2==1:
             Debit(acc)
         elif ch2==2:
             credit(acc)
         elif ch2==3:
             chbalance(acc)
         elif ch2==4:
             update(acc)
         elif ch2==5:
             main_menu()
         else:
             print("PLEASE SIGNUP FIRST!!NO SUCH USER ACCOUNT EXISTS")
         db.close()
def Debit(acc):
    db=shelve.open(".\initial_details",writeback=True)
    amt=int(input("Enter Amount to  be  debited:"))
    db['acc']['balance']+=amt
    print("Your current balance is ",db['acc']['balance'])
    db.close()
def credit(acc):
    db=shelve.open("./initial_details")
    amt=int(input("Enter amount to be credited:"))
    if db['acc']['password']>100:
        db['acc']['balance']-=amt
    print("Your current balance is ",db['acc']['balance'])
    db.close()
def chbalance(acc):
    db=shelve.open(".\initial_details")
    print("Here you go.....")
    print("Your current balance is ",db['acc']['balance'])
    db.close()
def update(acc):
    while True:

        new=input("Enter your new password:")
        rnew=input("Re-type your password:")
        if new==rnew:

            db=shelve.open(".\initial_details",writeback=True)
            db['acc']['password']=new
            print("Password changed successfully")
            db.close()


    
