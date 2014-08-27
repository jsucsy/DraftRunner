'''
Created on Aug 19, 2014

@author: jsu
'''

class Points():
    def __init__(self):
        self.pass_yds = 0
        self.pass_yds_300 = 0
        self.pass_yds_400 = 0
        self.pass_td = 0
        self.int_thrown = 0
        self.rush_yds = 0
        self.rush_yds_100 = 0
        self.rush_yds_175 = 0
        self.rush_td = 0
        self.reception = 0
        self.recep_yds = 0
        self.recep_yds_100 = 0
        self.recep_yds_175 = 0
        self.recep_td = 0
        self.twopt_conv = 0
        self.fumble_lost = 0
        self.off_fumble_ret_td = 0
        self.pick_six_thrown = 0
        self.fg_19 = 0
        self.fg_29 = 0
        self.fg_39 = 0
        self.fg_49 = 0
        self.fg_50 = 0
        self.fgmiss_19 = 0
        self.fgmiss_29 = 0
        self.fgmiss_39 = 0
        self.fgmiss_49 = 0
        self.pat_made = 0
        self.pat_miss = 0
        self.sack = 0
        self.int_recv = 0
        self.fumble_recv = 0
        self.def_td = 0
        self.def_safety = 0
        self.block_kick = 0
        self.spec_td = 0
        self.ptsallow_0 = 0
        self.ptsallow_6 = 0
        self.ptsallow_13 = 0
        self.ptsallow_20 = 0
        self.ptsallow_27 = 0
        self.ptsallow_34 = 0
        self.ptsallow_35 = 0
        
        self.idp_tack_solo = 0
        self.idp_tack_assist = 0
        self.idp_sack= 0
        self.idp_int= 0
        self.idp_fumble_force = 0
        self.idp_fumble_recv = 0
        self.idp_td = 0
        self.idp_safety = 0
        self.idp_block_kick = 0
        
        self.rostered_qb = 0
        self.rostered_rb = 0
        self.rostered_wr = 0
        self.rostered_te = 0
        self.rostered_ki = 0
        self.rostered_df = 0
        self.rostered_dp = 0
        self.rostersize = 0
        
    def check_zeros(self):
        zeros = []
        for key in self.__dict__.keys():
            if self.__dict__[key] == 0:
                zeros.append(key)
        
        return zeros
        
#-------------scoring------------------
             
def score_bu():
    points = Points()
    points.pass_yds = 0.04
    points.pass_yds_300 = 3
    points.pass_yds_400 = 2
    points.pass_td = 6
    points.int_thrown = -2
    points.rush_yds = 0.1
    points.rush_yds_100 = 3
    points.rush_yds_175 = 2
    points.rush_td = 6
    points.reception = 1
    points.recep_yds = 0.1
    points.recep_yds_100 = 3
    points.recep_yds_175 = 2
    points.recep_td = 6
    points.twopt_conv = 2
    points.fumble_lost = -2
    points.off_fumble_ret_td = 6
    points.pick_six_thrown = -2
    points.fg_19 = 3
    points.fg_29 = 3
    points.fg_39 = 3
    points.fg_49 = 4
    points.fg_50 = 5
    points.fgmiss_19 = -1
    points.fgmiss_29 = -1
    points.fgmiss_39 = -1
    points.fgmiss_49 = -1
    points.pat_made = 1
    points.pat_miss = -1
    points.sack = 1
    points.int_recv = 2
    points.fumble_recv = 2
    points.def_td = 6
    points.def_safety = 2
    points.block_kick = 2
    points.spec_td = 6
    points.ptsallow_0 = 7
    points.ptsallow_6 = 5
    points.ptsallow_13 = 3
    points.ptsallow_20 = 1
    points.ptsallow_27 = 0
    points.ptsallow_34 = -1
    points.ptsallow_35 = -3
    
    points.rostered_qb = 19
    points.rostered_rb = 50
    points.rostered_wr = 50
    points.rostered_te = 21
    points.rostered_ki = 14
    points.rostered_df = 16
    points.rostered_dp = 0
    points.rostersize = 17
    
    zeros = points.check_zeros()
    
    if zeros != []:
        print "Zero points assigned for: "
        for zero in zeros:
            print zero
    
    return points

def score_liz():
    points = Points()
    points.pass_yds = 0.04
    points.pass_td = 4
    points.int_thrown = -1
    points.rush_yds = 0.1
    points.rush_td = 6
    points.recep_yds = 0.1
    points.recep_td = 6
    points.twopt_conv = 2
    points.fumble_lost = -2
    points.off_fumble_ret_td = 6
    points.fg_19 = 3
    points.fg_29 = 3
    points.fg_39 = 3
    points.fg_49 = 4
    points.fg_50 = 5
    points.pat_made = 1
    points.sack = 1
    points.int_recv = 2
    points.fumble_recv = 2
    points.def_td = 6
    points.def_safety = 2
    points.block_kick = 2
    points.spec_td = 6
    points.ptsallow_0 = 10
    points.ptsallow_6 = 7
    points.ptsallow_13 = 4
    points.ptsallow_20 = 1
    points.ptsallow_27 = 0
    points.ptsallow_34 = -1
    points.ptsallow_35 = -4
    
    points.idp_tack_solo = 1
    points.idp_tack_assist = 0.5
    points.idp_sack= 2
    points.idp_int= 3
    points.idp_fumble_force = 1
    points.idp_fumble_recv = 1
    points.idp_td = 6
    points.idp_safety = 2
    points.idp_block_kick = 1

    points.rostered_qb = 21
    points.rostered_rb = 47
    points.rostered_wr = 37
    points.rostered_te = 19
    points.rostered_ki = 15
    points.rostered_df = 17
    points.rostered_dp = 17
    points.rostersize = 17
    
    '''
    zeros = points.check_zeros()
    
    if zeros != []:
        print "Zero points assigned for: "
        for zero in zeros:
            print zero
    '''
    
    return points
