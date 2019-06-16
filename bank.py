import time
def menu(acc_no):
    update_log("INFO","Application Started")
    s=""" 1.Debit\n 2.Credit\n 3.Check balance\n 4.Update password\n 5.Exit"""
    print(s)
    ch1=int(input("Enter your choice:"))
    if ch1==1:
        Debit(acc_no)
    elif ch1==2:
        Credit(acc_no)
    elif ch1==3:
        Check_bal(acc_no)
    elif ch1==4:
        up_passw(acc_no)
    else:
        main_menu()
def Debit(acc_no):
    amount=int(input("Enter amount to be debited:"))
    update_log("INFO",f"user has debited {amount} from account {acc_no}")
    db=shelve.open("bankwarehouse/bank.db",writeback=True)
    if amount<=db[acc_no]['bal']:
        db[acc_no]['bal']-=amount
        print("Your current balance is ",db[acc_no]['bal'])
    else:
        print("NO SUFFICIENT BALANCE AVAILABLE!!")
    db.close()
    time.sleep(5)
    
    menu(acc_no)
def Credit(acc_no):
    db=shelve.open("bankwarehouse/bank.db",writeback=True)
    cr_amt=eval(input("enter the amount to be credited:"))
    update_log('INFO',f"user has credited {cr_amt} to his account {acc_no}")
    if cr_amt>0:
        db[acc_no]['bal']+=cr_amt
        print(f"Amount credited to {acc_no} :{cr_amt}")
        print("Total amount",db[acc_no]['bal'])
    else:
        print("Not appropriate")
    db.close()
    time.sleep(5)
    menu(acc_no)
def Check_bal(acc_no):
    update_log('INFO',f"Balance Enquiry by user account {acc_no}")
    db=shelve.open("bankwarehouse/bank.db")
    dataa=db[acc_no]['bal']
    print("BALANCE-->",dataa)
    db.close()
    time.sleep(5)
    print("*"*120)
    menu(acc_no)
def up_passw(acc_no):
    update_log('INFO',f"Password updated by the user account {acc_no}")
    db=shelve.open("bankwarehouse/bank.db",writeback=True)
    from getpass import getpass
    new_pass=getpass("enter new password:")
    retypepass=getpass("Re-type your password:")
   
    if new_pass==retypepass:
        
        print("Your password has been changed succesfully!!")
        db[acc_no]['password']=new_pass
    else:
        print("Password does not match")
        up_passw(acc_no)
    db.close()
    menu(acc_no)
def main_menu():
    print('*'*120)
    s="""1.LOGIN\n 2.SIGNUP\n 3.EXIT"""
    print(s)
    ch=int(input("enter your choice:"))
    if ch==1:
        login() 
    elif ch==2:
        signup()
    else:
        pass
def login():
    acc_no=input("Enter your account number: ")
    passw=input("Enter your password:")
    db = shelve.open("bankwarehouse/bank.db",writeback=True)
    
        
    if acc_no in db and db[acc_no]['password']==passw:
        print("You have been successfully logged in")
        update_log('STATUS',f"User logged in to his account {acc_no}")
        menu(acc_no)
    else:
        print("Invaid password!! Try again ")
        update_log('WARNING',f"User tried an invalid password")
    db.close()
def signup():
    db=shelve.open("bankwarehouse/bank.db",writeback=True)
    name=input("Enter your name:")
    bal=eval(input("Enter balance:"))
    password=input("Enter your password:")
    acc=int(db['last_acc'])
    acc=str(acc+1)
    db['last_acc']=acc
    user={'name':name,'bal':bal,'password':password}
    db[acc]=user
    print("User account created successfully")
    update_log('STATUS',f"New account has been created {acc}")
    print("Note down your account number",acc)
    db.close()    
def update_log(logtype,message):
    s=f"{time.ctime()}:{logtype}--{message}"
    fp=open("log.txt",'a')
    fp.write(s)
    fp.close
main_menu()    
f=open('log.txt')
data=f.read()
print(data)
f.close()



200
