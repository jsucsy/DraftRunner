'''
Created on Aug 19, 2014

@author: jsu
'''
import config as c
import cPickle as pickle
import os, platform
from team import Team
import playerclass
import scoring as scoring

#-------------draft setup------------------------
def parse_yahoo_qb(sourcefile):
    players = []
    with open(sourcefile, 'rb+') as source:
        linenum = 0
        for line in source:
            if linenum == 0:
                continue
            else:
                fields = line.split('|')
                player = playerclass.Player(fields[0])
                player.set_yahoo_qb(fields[1], fields[2], fields[3], fields[4], 
                                 fields[5], fields[6], fields[7], fields[8], 
                                 fields[9], fields[10], fields[11])
                player.project_yahoo(c.points)
                players.append(player)
                
def choose_scoring():
    print '0: BU keeper'
    print '1: big dog expensive'
    print '2: work'
    print '3: Liz'
    
    scoring_option = raw_input('Choose Scoring Settings: ')
    
    if scoring_option == '0' or 0:
        c.points = scoring.score_bu()
    else:
        print 'No scoring setup for that option'

         
#-----------------live draft----------------------


#-----------------housekeeping--------------------

def setnode():
    if platform.node() == 'JoshLaptop':
        c.workingdir = 'c:\\users\\josh\\dropbox\\football\\temp\\'
        
def exclude():
    exclude = ['Team', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'os', 'pickle', 'platform', 'playerclass']
    return exclude

#-----------------tests---------------------------
def testall():
    test_setup()
    
    
def test_setup():
    setnode()
    


if __name__ == '__main__':
    testall()
