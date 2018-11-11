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
from TeamClass import MatchResult

def CheckStats(TeamAName, TeamBName, TeamAScore, TeamBScore):
    #print(TeamAName, TeamBName, TeamAScore, TeamBScore)
    outputreturnvalue = MatchResult()
    
    #check user didn't choose same team, otherwise return exception that's easy for main GUI to catch
    if TeamAName == TeamBName:
        return None
    
    #need to calculate which team won
    if TeamAScore > TeamBScore:
        #teamA won
        outputreturnvalue.TeamAWin = 1
        outputreturnvalue.TeamBWin = -1
        
        #score = win/loss * 0.01 of score differential
        outputreturnvalue.TeamAOutputNetScore = outputreturnvalue.TeamAWin+(0.01*abs(TeamAScore-TeamBScore))
        outputreturnvalue.TeamBOutputNetScore = outputreturnvalue.TeamBWin-(0.01*abs(TeamAScore-TeamBScore))
        outputreturnvalue.WinningTeam = TeamAName
        
    else:
        #teamB won
        outputreturnvalue.TeamAWin = -1
        outputreturnvalue.TeamBWin = 1
        
        #score = win/loss * 0.01 of score differential        
        outputreturnvalue.TeamBOutputNetScore = outputreturnvalue.TeamBWin+(0.01*abs(TeamAScore-TeamBScore))
        outputreturnvalue.TeamAOutputNetScore = outputreturnvalue.TeamAWin-(0.01*abs(TeamAScore-TeamBScore))
        outputreturnvalue.WinningTeam = TeamBName
        
    
    return outputreturnvalue
    


    
if __name__ == '__main__':
        tempresult = 5
        dictionarysequence = []
        
        teamlist1 = TeamListGenerator1(tempresult)
        print('teamlist1 = ', teamlist1)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        