'''
Created on Aug 19, 2014

@author: jsu
'''

class Player:
    '''field names starting with y = yahoo, e = espn, f = fftoday'''
    def __init__(self, name=''):
        self.name = name
        self.y_proj = 0
        self.e_proj = 0
        self.f_proj = 0
        
        self.y_pctown = 0
        self.y_games = 0
        self.y_pass_att = 0
        self.y_pass_comp = 0        
        self.y_pass_yds = 0
        self.y_pass_yds_300 = 0
        self.y_pass_yds_400 = 0
        self.y_pass_td = 0
        self.y_int_thrown = 0
        self.y_rush_att = 0
        self.y_rush_yds = 0
        self.y_rush_yds_100 = 0
        self.y_rush_yds_175 = 0
        self.y_rush_td = 0
        self.y_reception = 0
        self.y_recep_yds = 0
        self.y_recep_yds_100 = 0
        self.y_recep_yds_175 = 0
        self.y_recep_td = 0
        self.y_twopt_conv = 0
        self.y_fumble_lost = 0
        self.y_off_fumble_ret_td = 0
        self.y_pick_six_thrown = 0
        self.y_fg_19 = 0
        self.y_fg_29 = 0
        self.y_fg_39 = 0
        self.y_fg_49 = 0
        self.y_fg_50 = 0
        self.y_fgmiss_19 = 0
        self.y_fgmiss_29 = 0
        self.y_fgmiss_39 = 0
        self.y_fgmiss_49 = 0
        self.y_pat_made = 0
        self.y_pat_miss = 0
        self.y_sack = 0
        self.y_int_recv = 0
        self.y_fumble_recv = 0
        self.y_def_td = 0
        self.y_def_safety = 0
        self.y_block_kick = 0
        self.y_spec_td = 0
        self.y_ptsallow_0 = 0
        self.y_ptsallow_6 = 0
        self.y_ptsallow_13 = 0
        self.y_ptsallow_20 = 0
        self.y_ptsallow_27 = 0
        self.y_ptsallow_34 = 0
        self.y_ptsallow_35 = 0

    def set_yahoo_qb(self, pctown = 0, games = 0, passatt = 0, passcomp = 0, passyds = 0,
                  passtd = 0, intthrown = 0, passyds_300 = 0, rushatt = 0, rushyds = 0, rushtd = 0):
        self.y_pctown = pctown
        self.y_games = games
        self.y_pass_att = passatt
        self.y_pass_comp = passcomp
        self.y_pass_yds = passyds
        self.y_pass_td = passtd
        self.y_int_thrown = intthrown
        self.y_pass_yds_300 = passyds_300
        self.y_rush_att = rushatt
        self.y_rush_yds = rushyds
        self.y_rush_td = rushtd
        
    def show(self):
        return 'Name:       %s\r\nYahoo Proj: %s\r\nESPN Proj:  %s\r\nFFT Proj:   %s\r\n' %(self.y_proj, self.e_proj, self.f_proj)
                  
                  
                  
    
