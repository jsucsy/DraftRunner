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
def parse_player_yahoo(sourcefile, player_type):
    players = []
    with open(sourcefile, 'rb+') as source:
        linenum = 0
        for line in source:            
            if linenum != 0:
                fields = line.split('|')
                player = playerclass.Player(fields[0])
                if player_type.upper() == 'QB': 
                    player.set_yahoo_qb(fields[1], fields[2], fields[3], fields[4], 
                                        fields[5], fields[6], fields[7], fields[8], 
                                        fields[9], fields[10], fields[11])
                if player_type.upper() == 'RB': 
                    player.set_yahoo_rb(fields[1], fields[2], fields[3], fields[4], 
                                        fields[5], fields[6], fields[7], fields[8], 
                                        fields[9])
                if player_type.upper() == 'WR': 
                    player.set_yahoo_wr(fields[1], fields[2], fields[3], fields[4], 
                                        fields[5], fields[6])
                if player_type.upper() == 'TE': 
                    player.set_yahoo_te(fields[1], fields[2], fields[3], fields[4], 
                                        fields[5], fields[6])
                if player_type.upper() == 'KI': 
                    player.set_yahoo_ki(fields[1], fields[2], fields[3], fields[4], 
                                        fields[5], fields[6], fields[7], fields[8], 
                                        fields[9], fields[10], fields[11], fields[12])
                if player_type.upper() == 'ID': 
                    player.set_yahoo_id(fields[1], fields[2], fields[3], fields[4], 
                                        fields[5], fields[6], fields[7])                
                    
                player.project_yahoo(c.points)                
                players.append(player)
            linenum += 1
            
    #print player_type
    players.sort(key=lambda tup: tup.y_proj)
    players.reverse()
    #for player in players[0:10]:
    #    print player.showsmall()
    return players
                
def setplayers():
    source_yahoo_qb = c.workingdir + '20140825_yahoo_qb.csv'
    source_yahoo_rb = c.workingdir + '20140825_yahoo_rb.csv'
    source_yahoo_wr = c.workingdir + '20140825_yahoo_wr.csv'
    source_yahoo_te = c.workingdir + '20140825_yahoo_te.csv'
    source_yahoo_ki = c.workingdir + '20140825_yahoo_ki.csv'
    source_yahoo_id = c.workingdir + '20140825_yahoo_id.csv'
    
    c.qb = parse_player_yahoo(source_yahoo_qb, 'QB')
    c.rb = parse_player_yahoo(source_yahoo_rb, 'RB')
    c.wr = parse_player_yahoo(source_yahoo_wr, 'WR')
    c.te = parse_player_yahoo(source_yahoo_te, 'TE')
    c.ki = parse_player_yahoo(source_yahoo_ki, 'KI')
    c.id = parse_player_yahoo(source_yahoo_id, 'ID')
    
def setscoring():
    print '0: BU keeper'
    print '1: big dog expensive'
    print '2: work'
    print '3: Liz'
    
    scoring_option = raw_input('Choose Scoring Settings: ')
    
    if scoring_option == '0' or 0:
        c.points = scoring.score_bu()
    elif scoring_option == '3' or 3:
        c.points = scoring.score_liz()
    else:
        print 'No scoring setup for that option'

def setteams():
    leagues = []
    for filename in os.listdir(c.workingdir + 'setup'):
        if 'teams' in filename:
            leagues.append(filename)
    
    for league in leagues:
        print "%s: %s" % (leagues.index(league), league)        
    leaguenum = int(raw_input('Select league number: '))
    
    with open(c.workingdir + 'setup\\%s' % leagues[leaguenum], 'rb+') as source:
        counter = 0
        for line in source:
            fields = line.split('|')
            teamtemp = Team(fields[0], fields[1], counter)
            c.teams.append(teamtemp)

def setrpval(player_type, numonroster, projection = 'y'):
    rplist = player_type[numonroster:numonroster+5]
    rpsum = 0.0 
    for player in rplist:
        if projection.lower() == 'y':
            rpsum += player.y_proj
        elif projection.lower() == 'e':
            rpsum += player.e_proj
        elif projection.lower() == 'f':
            rpsum += player.f_proj
        else:
            print "Nothing set for projection type %s" % projection
            return 0
    
    return rpsum / 5    
    
def setrpvals():
    c.qbrp = setrpval(c.qb, c.points.rostered_qb, 'y')
    c.rbrp = setrpval(c.rb, c.points.rostered_rb, 'y')
    c.wrrp = setrpval(c.wr, c.points.rostered_wr, 'y')
    c.terp = setrpval(c.te, c.points.rostered_te, 'y')
    c.kirp = setrpval(c.ki, c.points.rostered_ki, 'y')
    c.idrp = setrpval(c.id, c.points.rostered_id, 'y')
    
    print "QB replacement val: %s" % c.qbrp
    print "RB replacement val: %s" % c.rbrp
    print "WR replacement val: %s" % c.wrrp
    print "TE replacement val: %s" % c.terp
    print "KI replacement val: %s" % c.kirp
    print "ID replacement val: %s" % c.idrp

def setvorp():
    for player in c.qb:
        player.y_vorp = player.y_proj - c.qbrp
    for player in c.rb:
        player.y_vorp = player.y_proj - c.rbrp
    for player in c.wr:
        player.y_vorp = player.y_proj - c.wrrp
    for player in c.te:
        player.y_vorp = player.y_proj - c.terp
    for player in c.ki:
        player.y_vorp = player.y_proj - c.kirp
    for player in c.id:
        player.y_vorp = player.y_proj - c.idrp
         
#-----------------live draft----------------------
def showqb(numtoshow = 5):
    print "Top %s QB: " % numtoshow
    for player in c.qb[0:numtoshow]:
        print player.showsmall()
def showrb(numtoshow = 5):
    print "Top %s RB: " % numtoshow
    for player in c.rb[0:numtoshow]:
        print player.showsmall()        
def showwr(numtoshow = 5):
    print "Top %s WR: " % numtoshow
    for player in c.wr[0:numtoshow]:
        print player.showsmall()        
def showte(numtoshow = 5):
    print "Top %s TE: " % numtoshow
    for player in c.te[0:numtoshow]:
        print player.showsmall()        
def showki(numtoshow = 5):
    print "Top %s KI: " % numtoshow
    for player in c.ki[0:numtoshow]:
        print player.showsmall()
def showid(numtoshow = 5):
    print "Top %s ID: " % numtoshow
    for player in c.id[0:numtoshow]:
        print player.showsmall()


def reco(numreco=5):
    '''recommend a player to draft'''
    topvorp = []
    for player in c.qb[0:numreco]:
        topvorp.append(player)
    for player in c.rb[0:numreco]:
        topvorp.append(player)
    for player in c.wr[0:numreco]:
        topvorp.append(player)
    for player in c.te[0:numreco]:
        topvorp.append(player)
    for player in c.ki[0:numreco]:
        topvorp.append(player)

    topvorp.sort(key=lambda tup: tup.y_vorp)
    topvorp.reverse()
    print "Recommended: "
    for player in topvorp[0:numreco]:
        print player.showsmall()

def setall():
    setnode()
    setscoring()
    setplayers()
    setteams()
    setrpvals()
    setvorp()
    
    reco(10)
    
    #showqb()
    #showrb()
    #showwr()
    #showte()
    #showki()
    
    

#-----------------housekeeping--------------------

def setnode():
    if platform.node() == 'JoshLaptop':
        #c.workingdir = 'c:\\users\\josh\\dropbox\\football\\data\\'
        c.workingdir = ''
        
def exclude():
    exclude = ['Team', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'os', 'pickle', 'platform', 'playerclass']
    return exclude

#-----------------tests---------------------------
def testall():
    test_setup()
    
def test_setup():
    setall()
    

if __name__ == '__main__':
    testall()
