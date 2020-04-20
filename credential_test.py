import unittest
from credential import Credential

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test case for the  credential class behaviour
    
    Args:
         unittest.Testcase:TestCase class that helps in the creating of test case
    '''
    
    def tearDown(self):
        '''
        tearDown method that cleans up after each test has run
        '''
        
        Credential.app_details=[]
    def setUp(self):
        '''
        set up method to run before each test
        '''
        
        self.new_credentail = Credential("app","password")
        
    def test_init(self):
        '''
        test_init test case if the opbject is initialized properly
        '''
        
        self.assertEqual(self.new_credentail.app,'app')
        self.assertEqual(self.new_credentail.password,'password')
        
    def test_save_app(self):
        '''
        Test_save_app test case to test if the app object is saved into the 
        credential list
        '''
        
        self.new_credentail.save_app()
        self.assertEqual(len(Credential.app_details),1)
        
    def test_delete_app(self):
        '''
        test_delete_app to test if we can remove credential from our credential list
        '''
        
        self.new_credentail.save_app()
        test_credential = Credential('instagram','ianshem1234')
        test_credential.save_app()
        
        self.new_credentail.delete_app()
        self.assertEqual(len(Credential.app_details),1)
        
        
    def test_find_app_name(self):
        
        '''
        test to check that we camn find the app with credentils
        
        '''
        
        self.new_credentail.save_app()
        test_credential = Credential('instagram','ianshem1234')
        test_credential.save_app()
        
        found_app = Credential.find_app('instagram')
        
        self.assertTrue(found_app,test_credential.app)
        
        
    def test_app_exist(self):
        
        '''
        Test to check if we can return a Boolean if we can't find the credential
        
        '''
        
        self.new_credentail.save_app()
        test_credential = Credential('instagram','ianshem1234')
        test_credential.save_app()
        
        apps_exist = Credential.find_app('instagram') 
        
        self.assertTrue(apps_exist)
        
    def test_display_app(self):
    

        '''
        method that returns a list of all app details saved
        '''

        self.assertEqual(Credential.display_app(),Credential.app_details)

        

if __name__ == "__main__":
    unittest.main()     
        
            
        
        
    

 