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
    
    

#module to test inputs, ensure proper formatting/usable

#results to test:
#If either Team A or Team B empty name, throw exception
#If either Team A or Team B empty score, throw exception

def CheckInputs(TeamAName, TeamBName, TeamAScore, TeamBScore):
    if TeamAName is None or TeamBName is None or TeamAScore is None or TeamBScore is None:
        #error code 1 = one of objects returned is None
        return 1
    
    if TeamAName or TeamBName or TeamAScore or TeamBScore == '':
        #error code 2 = one of objects is empty
        return 2

    if TeamAName == TeamBName:
        #error code 3 = name matching incorrectly
        return 3

    if TeamAScore == TeamBScore:
        #error code 4 = same score incorrect
        return 4
    
    else:
        return None

    
if __name__ == '__main__':
    print(CheckInputs('teama', 'teamb', 10, 15))




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        