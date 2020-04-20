import unittest
from user import User

class TestContact(unittest.TestCase):
    '''
    Test class that defines test case for user class behaviour
    Args:
        unittest.TestCase:TestCase class that helps in the creating of test case
    '''
    
def tearDown(self):
    '''
    tearDown method that does clean up afer each test has run
    '''
    
    User.user_list=[]
    
def setUp(self):
    '''
    set up method to run before each test
    '''   
    
    self.new_user = User('ian','shem','Ianshem1234')
    
def test_init(self):
    '''
    test_init test case if the opbject is initialized properly
    '''
    
    self.assertEqual(self.new_user.first_name,'ian')
    self.assertEqual(self.new_user.last_name,'shem')
    self.assertEqual(self.new_user.password,'Ianshem1234') 
           
def test_save_user(self):
    '''
    Test_save_user test case to test if the app object is saved into the 
    user list
    '''
    
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)
    
def test_delete_user(self):
    '''
    test to remove users from our user list 
    '''
    self.new_user.save_user()
    test_user = User('ian','shem','Ianshem1234')
    test_user.save_user()
    
    self.new_user.delete_user()
    self.assertEqual(len(User.user_list),1)
    
    
def test_find_user_by_first_name(self):
    '''
    test to find user with there first name inour user list 
    '''
    
    self.new_user.save_user()
    test_user = User('ian','shem','Ianshem1234')
    test_user.save_user()
    
    find_user = User.find_user_by_first_name('ian')
    
    self.assertEqual(find_user.password,test_user.password)
    

def test_user_exist(self):
    
    '''
    test to check if we can return a  boolean if we cannot find user
    
    '''
    
    self.new_user.save_user()
    test_user = User('ian','shem','Ianshem1234')
    test_user.save_user()
    
    user_exists = User.user_exist('ian')
    
    self.asserTrue(user_exists)
    
    
def test_display_user(self):
    
    '''
    method that returns a list of all user saved
    '''


    self.assertEqual(User.display_users(),User.user_list)





if __name__ == '__main__':
    unittest.main()      
    
    

            