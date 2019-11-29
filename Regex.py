#importing regex module
import re


#function to check for valid emails
def emailcheck(e_list):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    for i in e_list:
        if re.search(regex,i):
            print(i)

#taking input from the users
if __name__ == '__main__':
    N= int(input("Enter the number of email addresses"))
    email_list=[]
    print("Enter emails you want to validate")
    for i in range(0,N):
        eid=input()
        email_list.append(eid)

    emailcheck(email_list)

