'''
Created on Oct 28, 2018

@author: Andy
'''
class TeamClass():
    '''
    classdocs
    '''

    def __init__(self):
        #self.teamname = [None]
        self.teamwins = 0
        self.teamlosses = 0
        self.teamscore = 0.00
        '''
        Constructor
        '''

        
if __name__ == '__main__':
    #assume user wants 7 teams
    userrequest = 7
    
    #initialize dictionary name identities of user requested size
    dictionarysequence = [None]*userrequest
    
    #populate with default team names into sequencer
    for i in range(userrequest):
        dictionarysequence[i] = ('Team'+str(i+1))
        
    print('dictionary sequencer = ',dictionarysequence)
    
    #create teamlist with team names from sequencer
    teamlist = dict.fromkeys(dictionarysequence, TeamClass())
    print('final teamlist = ', teamlist)
    
    #confirm that all team names correctly input from sequencer
    print('mydict keys', teamlist.keys())
    
    #confirm how many teams are in dictionary
    print('mydict key length = ', len(teamlist.keys()))
    
    #need to iterate through dict and populate with default values
    #ignore, automatically populate in class initialization
    
    
    #iterate through each dict entry
    for i in range(len(teamlist.keys())):
        
        #get the team name to modify specified team stats
        print('dictionary sequence value = ', dictionarysequence[i])
        
        
        #example of modifying value of statistic in the class within a dict.
        teamlist[str(dictionarysequence[i])].teamwins = i
        
        #not possible to use stringvar, must have master in a Tk session
        #print result to confirm property modified by prior line
        print('team wins = ', teamlist[str(dictionarysequence[i])].teamwins)




    #how to iterate through each class object in class? wins, losses, score
    
    