import random
import string
class Credential:
    '''
    class that generates new passwords 
    '''
    
    app_details = []
    
    
    def __init__(self,app,app_password):
        
        self.app = app
        self.password = app_password
        
        
    def save_app(self):
        
        '''
        save_app saves credentials in the app_details
        '''
        self.app_details.append(self)
        
    def delete_app(self):
        '''
        delete_app method deletes a saved credential in the credential_list
        '''
        self.app_details.remove(self)
    
    
    @classmethod
    def find_app(cls,app):
        '''
        method that takes in app name and reurns the credentilas that matches the Credentials
        
        Args:
            credential: app name to search for
            
        Returns:
              app details of person that matches the credential.
              
        '''
        
        
        for Credential in cls.app_details:
            if Credential.app == app:
                return True
    
    @classmethod
    def app_exists(cls,app):
        
        '''
        Method that checks if a credentials exists from the ccredential list.
        Args:
            number: Phone number to search if it exists
            
        Returns:
               Boolean: True or false depending if the contact exists
               
        '''
        
        for Credential in cls.app_details:
            if Credential.app == app:
                return True
            
            return False
        
    @classmethod
    def gen_password(self):
    
    
        char = string.ascii_uppercase + string.ascii_lowercase
        gen_password = ''.join(random.choice(char) for i in range(0, 9))
        return gen_password
    
    @classmethod
    def display_app(cls):

        '''
        method that returns the app details
        '''

        return cls.app_details
    
    
                        