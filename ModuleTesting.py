'''
Created on Nov 10, 2018

@author: Andy
'''
import unittest
from UpdateStats import CheckInputs
from TeamListGenerator import TeamListGenerator1

class Test(unittest.TestCase):

    
    def setUp(self):
        #specify maximum user inputs
        self.userinputteams = 10
        
        self.totalteams = TeamListGenerator1(self.userinputteams)
        #create list of team names based on user input
        self.teamlist = list(self.totalteams.keys())
        print('self.teamlist = ', self.teamlist)
       
        

    def tearDown(self):
        pass


    def testName(self):
        pass
    
    def testmismatchinputs(self):
        #check for all possible inputs that logic returns correct response
        
        
        for i in range(len(self.teamlist)):
            print(self.teamlist[i])
            print(self.teamlist[len(self.teamlist)-1])
            print(CheckInputs(self.teamlist[i], self.teamlist[len(self.teamlist)-1], 15, 10))

            #self.assertEqual(CheckInputs((self.teamlist[i]), self.teamlist[len(self.teamlist)-1], 10, 15), None, 'something broke')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()