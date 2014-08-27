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
from datetime import datetime

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
                                        fields[9], fields[10], fields[11], fields[12])
                if player_type.upper() == 'RB': 
                    player.set_yahoo_rb(fields[1], fields[2], fields[3], fields[4],
                                        fields[5], fields[6], fields[7], fields[8],
                                        fields[9], linenum)
                if player_type.upper() == 'WR': 
                    player.set_yahoo_wr(fields[1], fields[2], fields[3], fields[4],
                                        fields[5], fields[6], linenum)
                if player_type.upper() == 'TE': 
                    player.set_yahoo_te(fields[1], fields[2], fields[3], fields[4],
                                        fields[5], fields[6], linenum)
                if player_type.upper() == 'KI': 
                    player.set_yahoo_ki(fields[1], fields[2], fields[3], fields[4],
                                        fields[5], fields[6], fields[7], fields[8],
                                        fields[9], fields[10], fields[11], fields[12], linenum)
                if player_type.upper() == 'ID': 
                    player.set_yahoo_dp(fields[1], fields[2], fields[3], fields[4],
                                        fields[5], fields[6], fields[7], linenum)
                    
                player.project_yahoo(c.points)                
                players.append(player)
            linenum += 1
            
    players.sort(key=lambda tup: tup.y_proj)
    players.reverse()
    return players
def setplayers():
    source_yahoo_qb = c.workingdir + '20140825_yahoo_qb.csv'
    source_yahoo_rb = c.workingdir + '20140825_yahoo_rb.csv'
    source_yahoo_wr = c.workingdir + '20140825_yahoo_wr.csv'
    source_yahoo_te = c.workingdir + '20140825_yahoo_te.csv'
    source_yahoo_ki = c.workingdir + '20140825_yahoo_ki.csv'
    source_yahoo_dp = c.workingdir + '20140825_yahoo_dp.csv'
    
    c.qb = parse_player_yahoo(source_yahoo_qb, 'QB')
    c.rb = parse_player_yahoo(source_yahoo_rb, 'RB')
    c.wr = parse_player_yahoo(source_yahoo_wr, 'WR')
    c.te = parse_player_yahoo(source_yahoo_te, 'TE')
    c.ki = parse_player_yahoo(source_yahoo_ki, 'KI')
    c.dp = parse_player_yahoo(source_yahoo_dp, 'ID')  
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
    for filename in os.listdir(c.workingdir + 'setup\\'):
        if 'teams' in filename:
            leagues.append(filename)
    
    for league in leagues:
        print "%s: %s" % (leagues.index(league), league)        
    leaguenum = int(raw_input('Select league number: '))
    
    with open(c.workingdir + 'setup\\%s' % leagues[leaguenum], 'rb+') as source:
        counter = 0
        for line in source:
            fields = line.split('|')
            teamtemp = Team(fields[0], fields[1], counter, c.points.rostersize)
            c.teams.append(teamtemp)
def setrpval(player_type, numonroster, projection='y'):
    rplist = player_type[numonroster:numonroster + 5]
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
    c.dprp = setrpval(c.dp, c.points.rostered_dp, 'y')
    
    print "QB replacement val: %s" % c.qbrp
    print "RB replacement val: %s" % c.rbrp
    print "WR replacement val: %s" % c.wrrp
    print "TE replacement val: %s" % c.terp
    print "KI replacement val: %s" % c.kirp
    print "ID replacement val: %s" % c.dprp
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
    for player in c.dp:
        player.y_vorp = player.y_proj - c.dprp
def setdrafttype():
    isauction = raw_input('Is draft an auction? y/n: ')
    if isauction.upper() == 'Y':
        c.auction = True
    elif isauction.upper() == 'N':
        c.auction = False
        rounds = c.points.rostersize
        teamcount = len(c.teams)
        for round in range(rounds):
            if round % 2 == 0:
                order = range(teamcount)                
            else:
                order = range(teamcount)
                order.reverse()
            for spot in order:
                c.draftorder.append(spot)
    else:
        print 'Please try again'
        setdrafttype()
def remove_drafted_player(player):
    if c.nom in c.qb:
        c.qb.remove(c.nom)
    elif c.nom in c.rb:
        c.rb.remove(c.nom)
    elif c.nom in c.wr:
        c.wr.remove(c.nom)
    elif c.nom in c.te:
        c.te.remove(c.nom)
    elif c.nom in c.ki:
        c.ki.remove(c.nom)
    elif c.nom in c.ds:
        c.ds.remove(c.nom)
    elif c.nom in c.dp:
        c.dp.remove(c.nom)
    else: 
        print "Player not found!!!!!"
        return 
    return

###-----------------backup and documentation--------
def backup():
    '''not working'''
    filename = c.workingdir + c.backup + '%s.pkl' % datetime.strftime(datetime.now(), '%Y%M%D%h%m')
    print 'Backup file: %s' % filename
    pickle.dump(c, filename)
    
    

###-----------------live draft----------------------

def showteams():
    for team in c.teams:
        print "%s: %s" % (c.teams.index(team), team.showsmall())
def showqb(numtoshow=5):
    print "Top %s QB: " % numtoshow
    for player in c.qb[0:numtoshow]:
        print player.showsmall()
def showrb(numtoshow=5):
    print "Top %s RB: " % numtoshow
    for player in c.rb[0:numtoshow]:
        print player.showsmall()        
def showwr(numtoshow=5):
    print "Top %s WR: " % numtoshow
    for player in c.wr[0:numtoshow]:
        print player.showsmall()        
def showte(numtoshow=5):
    print "Top %s TE: " % numtoshow
    for player in c.te[0:numtoshow]:
        print player.showsmall()        
def showki(numtoshow=5):
    print "Top %s KI: " % numtoshow
    for player in c.ki[0:numtoshow]:
        print player.showsmall()
def showdp(numtoshow=5):
    print "Top %s ID: " % numtoshow
    for player in c.dp[0:numtoshow]:
        print player.showsmall()
def nomq(name=''):
    nominate(name, c.qb)
def nomr(name=''):
    nominate(name, c.rb)
def nomw(name=''):
    nominate(name, c.wr)
def nomt(name=''):
    nominate(name, c.te)
def nomk(name=''):
    nominate(name, c.ki)
def nomd(name=''):
    nominate(name, c.ds)
def nomp(name=''):
    nominate(name, c.dp) 
def nominate(name, playerlist):
    nomtemp = []
    for player in playerlist:
        if name.upper() in player.name.upper():
            nomtemp.append(player)
            
    if len(nomtemp) == 0:
        print "No player found, try again"
    if len(nomtemp) == 1:
        c.nom = nomtemp[0] 
    if len(nomtemp) > 1:
        print "More than one found, choose a number: "
        for player in nomtemp:
            print "%s: %s" % (nomtemp.index(player), player.showsmall())
        playernum = int(raw_input('Player number: '))
        c.nom = nomtemp[playernum]
    print c.nom.showsmall()
    return

def reco(numreco=25):
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
        print "%s: %s" % (topvorp.index(player), player.showsmall())
    try:
        playernum = int(raw_input('Nominate player, enter for none: '))
    except ValueError:
        playernum = ''
    
    if playernum == '':
        return
    else:
        c.nom = topvorp[playernum]
        print c.nom.showsmall()
        return

def snake():
    cost = 0
    team = c.teams[c.draftorder[0]]
    print "\r\n Now drafting: %s" % team.showsmall()
    if c.nom == '':
        reco(25)
    if c.nom == '':
        return
    
    team.draft(c.nom, 0)
    c.drafted.append("%s|%s|%s|" % (team.showsmall(), cost, c.nom.showsmall()))
    print "\r\n%s drafts %s\r\n" % (team.name, c.nom.name)
    c.justwent = c.draftorder.pop(0)
    remove_drafted_player(c.nom)
    
    c.nom = ''
    
    snake()
    return

def history(numtoshow=len(c.drafted)):
    for line in c.drafted[-numtoshow:]:
        print line

def undo():
    '''puts all players into c.qb: need to add correct sorting logic'''
    lastdraft = c.drafted[-1]
    fields = lastdraft.split('|')
    print "\r\nUndrafting %s to %s\r\n" % (fields[6], fields[0])
    for teamtemp in c.teams:
        if teamtemp.name == fields[0]:
            team = teamtemp
    for playertemp in team.players:
        if playertemp.name == fields[6]:
            player = playertemp
    
    c.qb.append(player)
    c.qb.sort(key=lambda tup: tup.y_proj)
    c.qb.reverse()

    team.players.remove(player)
    c.drafted.pop()
    if c.justwent == '':
        showteams()
        c.justwent = int(raw_input("Select team number to draft next: "))        
    c.draftorder.insert(0, c.justwent)
    c.justwent = ''
    history(5)
       
def draft(team='', cost=''):
    '''
    if c.auction == True:
        if team == '':
            for team in c.teams:
                print "%s: %s" % (c.teams.index(team), team.showsmall())
            teamnum = int(raw_input('Choose team number: '))
            team = c.teams[teamnum]
        if cost == '':
            cost = int(raw_input('Enter bid price: '))
    
    for team_perm in c.teams:
        if team_perm == team:
            team_perm.draft(c.nom, cost)
    
    c.drafted.append("%s|%s|%s|" % (team.showsmall(), cost, c.nom.showsmall()))
    

    '''
    
    
def setall():
    # setnode()
    setscoring()
    setplayers()
    setteams()
    setdrafttype()
    setrpvals()
    setvorp()
    
    reco(25)
    
    # showqb()
    # showrb()
    # showwr()
    # showte()
    # showki()
    
    

#-----------------housekeeping--------------------

def setnode():
    if platform.node() == 'JoshLaptop':
        # c.workingdir = 'c:\\users\\josh\\dropbox\\football\\data\\'
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
