'''
Created on Oct 27, 2018

@author: Andy
'''


def TeamListGenerator(InitialVariable, Teams, TeamStats):
    
    #if requsted amount of teams exceed current list size, delete extras
    if len(InitialVariable) > Teams:
        print('current list exceeds requested size')
        print('teams = ', Teams)
        print('len initialvar = ', len(InitialVariable))
        print('initialvar = ', InitialVariable)
        del InitialVariable[Teams: len(InitialVariable)]
        print('returning result of length', len(InitialVariable))
        return InitialVariable
        
    else: 
        for i in range(len(InitialVariable), Teams):
            #print('teams = ', Teams)
            #print('Teamstats = ', TeamStats)
            InitialVariable.append(['empty']*TeamStats)
            
        return InitialVariable
        









if __name__ == '__main__':
    test = [[None, None, None, None], [None, None, None, None], [None, None, None, None]]
    #del test[5:6]
    #print(test)
    
    #print('test = ', test)
    test = TeamListGenerator(test, 5, 5)
    print('result length = ', len(test))
    #print('result[i] length = ', len(test[0]))
    print('result = ', test)