'''
Created on Aug 15, 2014

@author: jsu
'''

class Team:
    def __init__(self, name='', owner='', id='', rostersize = 17, budget = 200):
        self.name = name
        self.owner = owner
        self.players = []
        self.id = id
        self.budget = budget
        self.rostersize = rostersize
        
    def name(self, name):
        self.name = name
        
    def owner(self, owner):
        self.owner = owner
        
    def show(self):
        print 'Name: %s' % self.name
        print 'Owner: %s' % self.owner
        print '# Players: %s' % len(self.players)
        print 'Budget: $%s' % self.budget
        
    def showsmall(self):
        return "%s|%s|%s|%s|" % (self.name, self.owner, len(self.players), self.budget)
        
    def draft(self, player, cost=0):
        self.players.append(player)
        self.budget -= cost
        
    def roster(self):
        print self.showsmall()
        for player in self.players:
            print player.showsmall()
