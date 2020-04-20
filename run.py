#!/usr/bin/env python3.6
from credential import Credential
from user import User

def create_user (fname,lname,password):
    
    '''
    function to create new user
    
    '''
    
    new_user = User('fname','lname','password')
    return new_user


def create_credentials(app,app_password):
    '''
    function to create new credential
    '''
    
    new_credential = Credential(app,app_password)
    
    return new_credential


def save_user_account(user):
    
    '''
    function to save new users
    
    '''
    
    user.save_user ()
    
    
def save_credentials(credential):
    '''
    Function to save users credential
    
    '''
    
    credential.save_app()
    
    
def app_exists(app):
    '''
    function to find if app exist
    '''
    
    return Credential.app_exists(app)

def display_app():
    
    '''
    function to display app details
    
    '''
    
    return Credential.display_app()

def generate_password():
    '''
    function generate password
    '''
    
    generate_password = Credential.gen_password()
    return generate_password


def delete_app(self):
    '''
    function to delete apps
    '''
    return Credential.delete_app(self)


def main():
    print ("***************************welcome to paasword locker,'\n' 'please enter your name ...........'")
    
    
    user_name = input().lower()
    
    
    
    while True:
        print('\n')
        print("*"*60)
        print("Create app password using this short code: 'mine' = your own password, 'gp' = to generate password")
        print("\n")
        
        password = input().lower()
        
        if password == 'mine':
            print("*************Enter your password**************")
            password = input()
            break
        
        
        elif password == 'gp':
            
            password = generate_password()
            break
        
        else:print("*******************Enter a valid password***************")
        print("\n")
        
        
        
        print(f"welcome {user_name}!")
        print("\n")
        
        
    while True:
        print("*"*60)
        print("use this short code: 'sc' = to save user credentials, 'dc' = to display your credentials, 'del' = to delete your credentials, exit = to exit the app")
        print("\n")
        short_code = input().lower()
        
        if short_code == 'sc':
            print("*"*60)
            print("*********Enter your new app name*********")

            app = input()
            
            
            while True:
                print('\n')
                print("****Enter your password, use this short code: 'mine' = to enter your password , 'gp' = to generate your password*******")
                
                password = input()
                
                if password == 'mine':
                    print("*"*60)
                    print("\n")
                    
                    
                    print("**********Enter your password***********")
                    app_password = input()
                    break
                elif password == 'gp':
                    print("*"*60)
                    print("\n")
                    
                    app_password = generate_password()
                    break
                
                else: print("*********Enter a valid short code***********")
                
            save_credentials(create_credentials(app,password))
            
            
            print(f"****New {app} account created!*******'\n'")
            print (f"password: {app_password}")
            
        elif short_code == 'dc':
            print("*"*60)
            print('\n')
            if app_exists(app):
                print("****This are the list of apps that exist***** ")
                
                for Credential in display_app():
                    
                    print(f"**{Credential.app}**")
                    
                     
            else:
                print("*********You have no saved apps********")
            
        elif short_code == 'del':
            print("*"*60)
            print("\n")
            
            
            print("***********Type the app you want to delete***********")
    
            app = input()
            
            
            delete = app.delete_apps()
            
            return delete
        
        
        elif short_code == 'exit':
            print("*"*60)
            print("\n")
            
            print("***********Thank you for using password locker***********")
            
            break
        
        else:
             ("*************Please Enter a valid short code***************")


if __name__== " __main__":
    
    main()         
                
         