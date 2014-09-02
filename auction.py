'''
Created on Aug 29, 2014

@author: josh
'''
import config_auc as c
import playerclass_auc as playerclass

def parseplayers(sourcefile):
    ''' parse consolidated player file into playerclass, populate player list in config'''
    with open(sourcefile, 'rb+') as source:
        linenum = 0
        for line in source:
            fields = line.split('|')
            if linenum == 0:
                #print fields
                fields
            else:
                player = playerclass.Player(fields)
                c.players.append(player)
            linenum += 1

def setplayers():
    '''load all players into memory'''
    source_off= c.workingdir + '20140828_consolidated_off.csv'
    parseplayers(source_off)
    
def setall():
    '''standardized entry point to load auction'''
    setplayers()
    showplayers()
    
def showplayers(numtoshow = 10):
    print c.players[0].show_hdr()
    for i in range(numtoshow):
        print sorted(c.players,key=lambda tup: tup.all_rank)[i].show()
        #print c.players[i].show()
        
if __name__ == '__main__':
    setall()