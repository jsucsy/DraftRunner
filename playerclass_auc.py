'''
Created on Aug 29, 2014

@author: josh
'''

class Player:
    def __init__(self, fields):
        '''initializes player based on consolidated fields:
        ['Column1', 'name', 'pos', 'team', 'overallRank', 'positionRank', 'passAtt', 'passComp', 
        'passIncomp', 'passYds', 'passTds', 'passInt', 'rushAtt', 'rushYds', 'rushTds', 'rec', 
        'recYds', 'recTds', 'returnTds', 'twoPts', 'fumbles', 'cost', 'risk', 'sdPts', 'sdPick', 
        'passAttPts', 'passCompPts', 'passIncompPts', 'passYdsPts', 'passTdsPts', 'passIntPts', 
        'rushAttPts', 'rushYdsPts', 'rushTdsPts', 'recPts', 'recYdsPts', 'recTdsPts', 'twoPtsPts', 
        'fumblesPts', 'projectedPts', 'upside', 'projectedCost']'''
        
        #move this range to bottom, expedient to work from headers
        self.pass_yds_pts = float(fields[28])
        self.pass_tds_pts = float(fields[29])
        self.pass_int_pts = float(fields[30])
        self.rush_yds_pts = float(fields[32])
        self.rush_tds_pts = float(fields[33])
        self.rec_comp_pts = float(fields[34])
        self.rec_yds_pts = float(fields[35])
        
        
        self.name = fields[1]
        self.pos = fields[2]
        self.team = fields[3]
        self.all_rank = int(fields[4])
        self.pos_rank = int(fields[5])
        self.pass_att = float(fields[6])
        self.pass_comp = float(fields[7])
        self.pass_incomp = float(fields[8])
        self.pass_yds = float(fields[9])
        self.pass_tds = float(fields[10])
        self.pass_int = float(fields[11])
        self.rush_att = float(fields[12])
        self.rush_yds = float(fields[13])
        self.rush_tds = float(fields[14])
        self.rec_comp = float(fields[15])
        self.rec_yds = float(fields[16])
        self.rec_tds = float(fields[17])
        self.return_tds = float(fields[18])
        self.two_pts = float(fields[19])
        self.fumbles = float(fields[20])
        self.avg_cost = float(fields[21])
        self.risk = float(fields[22])
        self.sd_pts = float(fields[23])
        self.sd_pick = float(fields[24])
         
        
    def show(self):
        return '|'.join(map(str,[self.name, self.pos, self.team, self.all_rank, self.pos_rank, self.avg_cost,
                                 self.risk, self.sd_pts, self.sd_pick]))
    
    def showall(self):
        '''not functional'''
        return '|'.join(map(str,self.__attr__))
    
    def show_hdr(self):
        return '|'.join(['name', 'pos', 'team', 'overallRank', 'positionRank', 'cost', 'risk', 'sdPts', 'sdPick'])
    
    def showall_hdr(self):
        return