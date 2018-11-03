'''
Created on Oct 25, 2018

@author: Andy
'''

import TeamListResult

if __name__ == '__main__':
    
    #mylist = ['team1', 'team2', 'team3', 'team4', 'lastteam']
    #print(mylist)
    
    #del mylist[2]
    #print(mylist)
    
    #del mylist[2:len(mylist)]
    #print(mylist)
    
    #mylist.append('secondlastteam')
    #print(len(mylist))
    #print(mylist)
    
    #for i in range(3,5):
    #    del mylist[3]
    #    print(mylist)
        
        
        
        #test if for example list of 20, if delete item 10, would next items increase by index of 1?
        
        
        
        
        
    #list to hold variables used for ttk.labels
    team = [['Team1']*3]*3
    print('team = ', team)
    
    teamsetup = []
    print('teamsetup = ', teamsetup)
    for i in range(10):
        teamsetup.append([])
        
    print('teamsetup finished = ', teamsetup)
    
    print('test generator')
    test = [[0 for j in range(3)] for i in range(5)]
    print(test)
        
        
        
    test2 = []
    
    #create 10 teams
    #each team will require the following: Team Name, Wins, Losses, Score
    
    for i in range(10):
        test2.append([('Team'+str(i+1),), 0, 0, 0])
        
    print(test2)
    print(test2[4][0])
        
        
        
        #list to hold name to be displayed in the label
    #teamname = ['Team1']*int(100)
    #print('teamname = ', teamname)