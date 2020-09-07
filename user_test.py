import unittest 
from user import User

class TestUser(unittest.TestCase):


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Patricia","Anduru","0704827097","andurupatricia@gmail.com","Patricia","4567") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Patricia")
        self.assertEqual(self.new_user.last_name,"Anduru")
        self.assertEqual(self.new_user.phone_number,"0704827097")
        self.assertEqual(self.new_user.email,"andurupatricia@gmail.com")
        self.assertEqual(self.new_user.username,"Patricia")
        self.assertEqual(self.new_user.password,"4567")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []


    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Patricia","Anduru","0704827097","andurupatricia@gmail.com","Patricia","4567") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Patricia","Anduru","0704827097","anduruptricia@gmail.com","Patricia","4567") # new user
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)
    def test_find_user_by_number(self):
        '''
        test to check if we can find a user by phone number and display information
        '''
        self.new_user.save_user()
        test_user = User("Patricia","Anduru","0704827097","andurupatricia@gmail.com","Patricia","4567") # new user
        test_user.save_user()

        found_user = User.find_by_number("0704827097")

        self.assertEqual(found_user.email,test_user.email)
        
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("Patricia","Anduru",")0704827097","andurupatricia@gmail.com","Patricia","4567") # new user
        test_user.save_user()

        user_exists = User.user_exist("0704827097")

        self.assertTrue(user_exists)
        
    def test_display_all_users(self):
        self.assertEqual(User.display_users(),User.user_list)


if __name__ == '__main__':
    unittest.main()