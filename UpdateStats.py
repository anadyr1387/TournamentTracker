'''
Created on Nov 2, 2018

@author: Andy
'''
#program to get the outputs to update the table
#given user input of teams A and B
#Returns team stats to modify
#returns both teams win/loss
#returns both teams Net score after game

from TeamListGenerator import TeamListGenerator1


def CheckStats(TeamAName, TeamBName, TeamAScore, TeamBScore):
    #print(TeamAName, TeamBName, TeamAScore, TeamBScore)

    TeamAWin = None
    TeamBWin = None
    TeamAOutputNetScore = None
    TeamBOutputNetScore = None
    WinningTeam = None
    
    #check user didn't choose same team, otherwise return exception that's easy for main GUI to catch
    if TeamAName == TeamBName:
        return None
    
    #need to calculate which team won
    if TeamAScore > TeamBScore:
        TeamAWin = 1
        TeamBWin = -1
        TeamAOutputNetScore = TeamAWin+(0.01*abs(TeamAScore-TeamBScore))
        TeamBOutputNetScore = TeamBWin-(0.01*abs(TeamAScore-TeamBScore))
        WinningTeam = TeamAName
        
    else:
        TeamAWin = -1
        TeamBWin = 1
        TeamBOutputNetScore = TeamBWin+(0.01*abs(TeamAScore-TeamBScore))
        TeamAOutputNetScore = TeamAWin-(0.01*abs(TeamAScore-TeamBScore))
        WinningTeam = TeamBName
        
    
    return [TeamAName, TeamBName, TeamAWin, TeamBWin, TeamAOutputNetScore, TeamBOutputNetScore, WinningTeam]
    



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
        tempresult = 5
        dictionarysequence = []
        
        #populate with default team names into sequencer
        
        #Sequence = [ 'Team%d' % (i + 1) for i in range(tempResult) ]
        
        
        
        
        
        
        
        for i in range(tempresult):
            dictionarysequence.append(str('Team'+str(i+1)))
            
        print(dictionarysequence)
        
        
        
        # need to use list comprehension more often
        #check if this works
        teamlist1 = TeamListGenerator1(tempresult)
        

        #for i in range(len(dictionarysequence)):
            
            #need to create loop to iteratively create TeamClass()
            #otherwise arguments evaluated prior to function call, so keeps calling same TeamClass() object for each dict 
        #    teamlist1 = dict.fromkeys(dictionarysequence[i], TeamClass())
        print('teamlist1 = ', teamlist1)
        #print(len(teamlist1))
        
        userinputa = dictionarysequence[1]
        userinputb = dictionarysequence[2]
        #print('userinput team a = ',userinputa)
        #print('userinput team b = ',userinputb)
        
        userinputascore = 35
        userinputbscore = 32
        #print('userinputscorea = ', userinputascore)
        #print('userinputscoreb = ', userinputbscore)
        resultant = CheckStats(userinputa, userinputb, userinputascore, userinputbscore)
        
        
        
        #check which team won
        #if Team A won
        print('resultant = ',resultant[5])
        print(userinputa)
        print(userinputb)
        
        teamlist1[userinputa].teamscore+=resultant[4]
        teamlist1[userinputb].teamscore+=resultant[5]
        
        
        print('teama score = ',teamlist1[userinputa].teamscore)
        print('teamb score = ', teamlist1[userinputb].teamscore)
        
        if userinputa == resultant[6]:
            print('team a won')
            #update team a score

            
            #we know that Team A won, so only update losses for Team B
            #update wins for Team A
            teamlist1[userinputa].teamwins+=1
            teamlist1[userinputb].teamlosses+=1
        
        #else we know that Team B won
        else:
            teamlist1[userinputa].teamlosses+=1
            teamlist1[userinputb].teamwins+=1
        
        
        print('teama wins = ', teamlist1[userinputa].teamwins )
        
        
        print('teamb losses = ', teamlist1[userinputb].teamlosses)
        print('teama losses = ', teamlist1[userinputa].teamlosses)
        
        #print('teama score = ', teamlist1[userinputa].teamscore)
        #print('teamb score = ', teamlist1[userinputb].teamscore)
        
        #keep sharing class data between 

        
        
        
        #print('teamlist = ', teamlist1[userinputa].teamscore)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        