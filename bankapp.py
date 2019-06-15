from auth import login
from signup import signup 
print("Welcome to MY bank")
s='''
1.Login
2.Signup
3.Exit
'''
print(s)
def main_menu():
        ch=int(input("Enter Your Choice"))
        if ch==1:

            login() 
        elif ch==2:
            signup()
        else:
            print("Successfully Exited")
main_menu()
