'''
Created on Oct 23, 2018

@author: Andy
'''

import sys
import tkinter as tk
from tkinter import ttk, StringVar
from PIL import Image, ImageTk
from TeamListGenerator import TeamListGenerator
from TeamClass import TeamClass
from UpdateStats import CheckStats

class NotebookDemo (ttk.Frame):
    
    def __init__(self, isapp=True, name='gui'):
        ttk.Frame.__init__(self, name=name)
        self.grid(row=0)
        self.master.title('Tournament Tracker')
    
        self._create_widgets()
        
    def _create_widgets(self):

        self.tempresult = 0
        
        inputsframe2 = ttk.Frame(relief='sunken', borderwidth='5')
        inputsframe2.grid(row=2)
        
        
        #labels to indicate to user what each field will be
        self.inputlabels = ["Number of Teams:", "Team A:", "Team B:", "Team A Score:", "Team B Score:"]   
        
        #actual inputs from user 
        self.labelinputs = ["Teams", "A_team", "B_team", "A_score", "B_score"]
        
        for i in range(len(self.inputlabels)):
            #print("Label " + str(i) + " = " + str(self.inputlabels[i]))
            #labelname = str('self.numberteamslabel')+str(i)
            #print(labelname)
            self.inputlabels[i] = ttk.Label(inputsframe2, text = str(self.inputlabels[i]))
            self.inputlabels[i].grid(column=1, row=i, sticky='w')
            #print('Input label names = '+str(self.inputlabels[i]))
            
            #labelinput = str()
            #print(labelinput)
            self.labelinputs[i] = ttk.Combobox(inputsframe2, width=10)
            self.labelinputs[i].grid(column=2, row=i, sticky='e', padx = 15)
            #print(self.labelinputs[i])
            #print("Input data names = "+str(self.labelinputs[i]))
            
        self.updateall = ttk.Button(inputsframe2, text='Update Team Number', command=lambda:self._updateinfo(self.teamspecificinfo))
        self.updateall.grid(column=3, row = 0)
        
        self.resetteams = ttk.Button(inputsframe2, text='Reset Information', command=self._resetteams)
        self.resetteams.grid(column=3, row = 1)
        
        self.resetitem = ttk.Button(inputsframe2, text='Get Team Names', command=self._getteamnames)
        self.resetitem.grid(column=3, row = 2)
        
        self.resetitem = ttk.Button(inputsframe2, text='Update All Statistics', command=self._updatestats)
        self.resetitem.grid(column=3, row = 3)
        
        #frame for holding team information
        self.inputsframe3 = ttk.Frame(relief='sunken', borderwidth='5')
        self.inputsframe3.grid(row=3)
        
        self.teamlabels = ttk.Frame(self.inputsframe3, relief = 'sunken', borderwidth = '5')
        self.teamlabels.grid(row=0)
        
        self.teamspecificinfo = ttk.Frame(self.inputsframe3, relief = 'sunken', borderwidth = '5')
        self.teamspecificinfo.grid(row=1, column=0, sticky='W', columnspan = 4)
        
        
        #labels for information displaying team specific items
        self.teamlabelsinfo1 = ['Team A Name', 'Team A Wins', 'Team A Losses', 'Team A Score'], ['Team B Name', 'Team B Wins', 'Team B Losses', 'Team B Score']
        
        #list to be appended to when adding team statistic information
        #self.teamlabelsinfo3 = []
        
        #amount of statistics to be associated with each team
        #self.statistics = 4
        
        #declare initial empty list to base generated list on.
        #self.teamdata = []
        #function to generate list based on requested size
        #self.temp = TeamListGenerator(self.temp, 5, self.statistics)
        #print(self.temp)
        
        #initialize list to be converted to StringVar(), must be initialized
        self.teamlabelsinfo2 = [None, None, None, None], [None, None, None, None]
        
        print('temlabelsinfo2 = ', self.teamlabelsinfo2)
        #print(self.teamlabelsinfo1[0][0])
        
        self.userinputs = [None]*5
        print('userinputs[3] = ', self.userinputs[3])
        
        
        
        
        print('len tamlabelsinfo1 = ' , len(self.teamlabelsinfo1))
        print('len teamlabelsinfo1[0] = ', len(self.teamlabelsinfo1[0]))
        
        #rows
        for i in range (len(self.teamlabelsinfo1)):
            #columns
            for j in range(len(self.teamlabelsinfo1[i])):
                #convert index item to StringVar
                self.teamlabelsinfo2[i][j] = StringVar()
                #set value of item to match list of list
                self.teamlabelsinfo2[i][j].set(self.teamlabelsinfo1[i][j])
                
                #one-time intialization labels, no external references
                b= ttk.Label(self.teamlabels, textvariable=str(self.teamlabelsinfo2[i][j]))
                b.grid(row=i, column=j, padx='5')
             

                
            #working example of reading from list, unable to use textvariable
            #may need to create separate frame for each type statistic to show, team name, score, etc.
            #self.teamlabelsinfo[i] = ttk.Label(self.teamlabels, text=str(self.teamlabelsinfo1[i][1]))
            #print((self.teamlabelsinfo1[i][0]))
            #self.teamlabelsinfo[i].grid(row=0, column=i)

        #list to hold variables used for ttk.labels
        
        #self.team = ['Team1']*int(1)
        #print(self.team)
        
        #list to hold name to be displayed in the label
        #self.teamname = ['Team1']*int(100)


        
        
    def _updateinfo(self, displayframe):

        #get first combobox entry (number of teams requested)
        #index 0 = teams to create
        self.tempresult = self.labelinputs[0].get()
        
        #initialize dictionary name identities of user requested size
        self.dictionarysequence = [None]*int(self.tempresult)
        
        #populate with default team names into sequencer
        for i in range(int(self.tempresult)):
            self.dictionarysequence[i] = ('Team'+str(i+1))
            
        #print('dictionary sequencer = ',self.dictionarysequence)
        
        #create dict teamlist with team names from sequencer
        self.teamlist1 = dict.fromkeys(self.dictionarysequence, TeamClass())
        print(self.teamlist1)

        #config comboboxes to allow for selection of existing teams.
        #index 0 = team selection
        #index 1 = team a
        #index 2 = team b
        #index 3 = comments, currently unused
        self._updatetable(displayframe)
        self.labelinputs[1].config(values=self.dictionarysequence)
        self.labelinputs[2].config(values=self.dictionarysequence)
        
        
        
    def _updatetable(self, displayframe):
                      
            
        #set column widths prior to inserting row information
        for j in range(4):
            displayframe.columnconfigure(j, minsize = '90')
        
        
        #rows
        for i in range(int(self.tempresult)):
            
            #columns
            #for j in range(4):
            #issue is from here, if select 5 teams and update
            #pressing update again will create another 5 labels????? with incremented numbers from previous update
            
            #this issue is still unresolved, will work on afterwards

            #4 times the amount of labels are being generated here
            #need to fix, runs slow
            b = ttk.Label(displayframe, text= str(self.dictionarysequence[i]), background = 'yellow')
            b.grid(row=i, column=0, sticky = 'w', padx = '5')
                            
                #team wins
            b = ttk.Label(displayframe, text= str(self.teamlist1[self.dictionarysequence[i]].teamwins), background = 'yellow')
            b.grid(row=i, column=1, sticky = 'w', padx = '5')
                            
                #team losses
            b = ttk.Label(displayframe, text= str(self.teamlist1[self.dictionarysequence[i]].teamlosses), background = 'yellow')
            b.grid(row=i, column=2, sticky = 'w', padx = '5')
                            
                #team score
            b = ttk.Label(displayframe, text= str(self.teamlist1[self.dictionarysequence[i]].teamscore), background = 'yellow')
            b.grid(row=i, column=3, sticky = 'w', padx = '5')
            
            
            
    def _resetteams(self):
        self.teamspecificinfo.destroy()
        self.teamspecificinfo = ttk.Frame(self.inputsframe3, relief = 'sunken', borderwidth = '5')
        self.teamspecificinfo.grid(row=1, column=0, sticky='W', columnspan = 4)
       
        #this runs horibly slow with 200+ label widgets
        #for i in range(len(self.teamspecificinfo.winfo_children())):
            #print(i)
            #self.team[0].destroy()
            #self.teamspecificinfo.winfo_children()[0].destroy()
            #print('widgets remaining', self.teamspecificinfo.winfo_children())
            #self.teamspecificinfo.update()
        
        
        
    def _getteamnames(self):
        #index 0 = team selection
        #index 1 = team a
        #index 2 = team b
        #index 3 = comments, currently unused
        print('getting team names')
        self._getinputs()
        
        #get team A selection
        print(self.userinputs[1])
        
        #get team B selection
        print(self.userinputs[2])
        
                
            
    def _updatestats(self):
        print('updating all statistics')
        self._getinputs()
        #get team A score input
        print(self.userinputs[3])
        
        #get team B score input
        print(self.userinputs[4])
        
        
    def _updateteamlist(self):
        pass
    
        
        
        
    def _getinputs(self):
        for i in range(len(self.labelinputs)):
            print(i)
            self.userinputs[i] = self.labelinputs[i].get()
        print(self.userinputs)
        
        

        
        
    def _getinputtext(self):
        pass
        #self.senttext = self.inputtext1.get()
        #server_requests.requestimage(self, self.senttext, self.videopanel)
            
    def _endclient(self):
        pass
        #server_requests.requestimage(self, 'end')
    

if __name__ == '__main__':
    NotebookDemo().mainloop()
    
    
    
    
    
    
    
    