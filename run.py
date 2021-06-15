#!/usr/bin/env python3.8
from user_login import User
import random
from user_login import Password

def register(username,password,accountName):
    user_details=User(username,password,accountName)
    return user_details
def save_user(user_login):
    user_login.register()

'''
Function to delete Account info
'''
def deletepassword(username,password,email):
    user_details=User(username,password,email)
    return user_details


def delete_account(user_login):
    user_login.delete_password()

"""
Display contacts
"""
def display_passwords():
    return User.display_user();


#Function to search password on specific Accounts

def search_accountPassword(number):
    return User.find_by_accountName(number);

def check_if_accountExist(number):
    return User.account_exist(number)

'''
This a function to generate random password
'''
def random_password(limit):
    password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(*&^%$#@!)"
    ran=len(password)
    hold=''
    for i in range(0,limit):
        all=password[random.randint(0,ran)]
        hold=hold+all
    return hold

def main():
        print("\n")
        print("WELCOME TO PASSWORD LOCKER ")
        print("\n")
        print("welcome to Password Locker.. Manage your passwords with ease")
        print("Please Register\n Enter your userName")
        name=input()
        print("Use g-generate password or m- to make your own password or press enter- to make your own password \U0001F606 ")
        short_codes=input().lower()
        if short_codes=="g":
            print("Enter the length that you would like your password to have. Recommended length:)5")
            limit=int(input())
            print('\n')
            print("**"*7)
            password = random_password(limit)
            print("Your password is "+password)
            print("**"*7)
        else:
            print("Enter your password")
            password=input()
        thisAccout="passwordLocker"
        save_user(register(thisAccout,password,name))
        print("\n")
        print(f"Welcome {name}! Please Login ")
        print("Enter your username that you just created above")
        User=input()
        print("enter your password")
        vPassword=input()
        if User ==name and vPassword==password:
            print("\n")
            print(f"Welcome to your dashboard {name}")
            while True:
                print("These are short keys to help you navigate through\n sp- save new password dp-- display all passwords fa-- find a specific account password  dp-- delete password x-- exit this application")
                short_codes=input().lower()
                if short_codes=="cp":
                    print("-"*10)
                    print("Ready to create new password\n")
                    print(f"{name}Please enter the account name you need to be saved  eg:-Instagram | Facebook | Twitter | Google+ | Pintrest")
                    thisAccout=input();
                    print("Enter username")
                    username=input();
                    print("Enter the password make sure no one is watching ")
                    password=input()
                    save_user(register(thisAccout,username,password))
                    print("\n")
                    print(f"{thisAccout} account details saved successfully")
                    print("\n")

                elif short_codes=="dc":
                    if display_passwords():
                        print(f"{name} This are all your passwords keep em save")
                        print("--"*40)
                        print("Account Name \t  Username\t password")
                        print("_"*60)
                        for account in display_passwords():
                            print(f"{account.username} \t {account.password}.......{account.email}")
                            print("\n")
                        print("--"*40)
                    else:
                        print("\n")
                        print("It seems you have not Accounts yet")
                elif short_codes=="fa":
                    print("Enter Account name")
                    search_pass=input();
                    if check_if_accountExist(search_pass):
                        searchP=search_accountPassword(search_pass)
                        print("\n")
                        print("Account Match ------1")
                        print("Username\t password")
                        print("__"*20)
                        print(f"{searchP.password}...\t{searchP.email}")
                        print("--"*20)
                        print("\n")
                    else:
                        print("That Account does not exist Please Try again")
                        print("--"*20)
                        print("\n")

                elif short_codes=="dl":
                    print("Enter Account Name to be deleted")
                    delAccount=input();
                    if check_if_accountExist(delAccount):
                        for i in display_passwords():
                            if delAccount in i.username:
                                posi=display_passwords().index(i)

                        # delete_account(posi)
                        display_passwords().remove(display_passwords()[posi])
                        print("\n")

                        print(f"{delAccount} Account deleted successfully")
                        print("\n")
                    else:
                        print("Oh!...an error occurred,That account does not exist")






                elif(short_codes == "ex"):
                    print("are you sure about this \n yes or no")
                    sure=input().lower()
                    if sure=="no":
                        continue
                    else:
                        print("Come Again!")
                        break
                else:
                    print("I didn't Get you would you mind using the short codes please")
        else:
            print("wrong username or password")
if __name__ == '__main__':
    main()
