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
        self.y_vorp = 0.0
        self.e_vorp = 0.0
        self.f_vorp = 0.0
        
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
        
        #individual defensive player
        self.y_idp_tack_solo = 0
        self.y_idp_tack_assist = 0
        self.y_idp_sack= 0
        self.y_idp_int= 0
        self.y_idp_fumble_force = 0
        self.y_idp_fumble_recv = 0
        self.y_idp_td = 0
        self.y_idp_safety = 0
        self.y_idp_block_kick = 0

    def set_yahoo_qb(self, pctown = 0, games = 0, passatt = 0, passcomp = 0, passyds = 0,
                  passtd = 0, intthrown = 0, passyds_300 = 0, rushatt = 0, rushyds = 0, rushtd = 0):
        self.y_pctown = float(pctown)
        self.y_games = float(games)
        self.y_pass_att = float(passatt)
        self.y_pass_comp = float(passcomp)
        self.y_pass_yds = float(passyds)
        self.y_pass_td = float(passtd)
        self.y_int_thrown = float(intthrown)
        self.y_pass_yds_300 = float(passyds_300)
        self.y_rush_att = float(rushatt)
        self.y_rush_yds = float(rushyds)
        self.y_rush_td = float(rushtd)
    
    def set_yahoo_rb(self, pctown = 0, games = 0, rush_att = 0, rush_yds = 0, rush_td = 0, 
                     rush_yds_100 = 0, reception = 0, recep_yds = 0, recep_td = 0):
        self.y_pctown = float(pctown)
        self.y_games = float(games)
        self.y_rush_att = float(rush_att)
        self.y_rush_yds = float(rush_yds)
        self.y_rush_td = float(rush_td)
        self.y_rush_yds_100 = float(rush_yds_100)
        self.y_reception = float(reception)
        self.y_recep_yds = float(recep_yds)
        self.y_recep_td = float(recep_td)
    
    def set_yahoo_wr(self, pctown = 0, games = 0, reception = 0, recep_yds = 0, recep_td = 0, recep_yds_100 = 0):
        self.y_pctown = float(pctown)
        self.y_games = float(games)
        self.y_reception = float(reception)
        self.y_recep_yds = float(recep_yds)
        self.y_recep_td = float(recep_td)
        self.y_recep_yds_100 = float(recep_yds_100)
    
    def set_yahoo_te(self, pctown = 0, games = 0, reception = 0, recep_yds = 0, recep_td = 0, recep_yds_100 = 0):
        self.y_pctown = float(pctown)
        self.y_games = float(games)
        self.y_reception = float(reception)
        self.y_recep_yds = float(recep_yds)
        self.y_recep_td = float(recep_td)
        self.y_recep_yds_100 = float(recep_yds_100)
        
    def set_yahoo_ki(self, pctown = 0, fg_att = 0, fg_made = 0, fg_att_29 = 0, fg_made_29 = 0,
                     fg_att_39 = 0, fg_made_39 = 0, fg_att_49 = 0, fg_made_49 = 0,
                     fg_att_50 = 0, fg_made_50 = 0, pat_made = 0):
        self.y_pctown = float(pctown)
        self.y_fg_29 = float(fg_made_29)
        self.y_fg_39 = float(fg_made_39)
        self.y_fg_49 = float(fg_made_49)
        self.y_fg_50 = float(fg_made_50)
        self.y_pat_made = float(pat_made)
        self.y_fgmiss_29 = float(fg_att_29) - float(fg_made_29)
        self.y_fgmiss_39 = float(fg_att_39) - float(fg_made_39)
        self.y_fgmiss_49 = float(fg_att_49) - float(fg_made_49)
        self.y_fgmiss_50 = float(fg_att_50) - float(fg_made_50)
        self.y_fg_19 = float(fg_made) - self.y_fg_29 - self.y_fg_39 - self.y_fg_49 - self.y_fg_50
        self.y_fgmiss_19 = (float(fg_att) - float(fg_made)) - self.y_fgmiss_29 - self.y_fgmiss_39 - self.y_fgmiss_49 - self.y_fgmiss_50
        
    def set_yahoo_id(self, pctown = 0, tack_solo = 0, tack_assist = 0, sack = 0, 
                     idp_int = 0, fumble_force = 0, pass_def = 0):
        
        self.y_pctown = float(pctown)
        self.y_idp_tack_solo = float(tack_solo)
        self.y_idp_tack_assist = float(tack_assist)
        self.y_idp_sack= float(sack)
        self.y_idp_int= float(idp_int)
        self.y_idp_fumble_force = float(fumble_force)
        
        
    def show(self):
        return 'Name:       %s\r\nYahoo Proj: %s\r\nESPN Proj:  %s\r\nFFT Proj:   %s\r\n' %(self.y_proj, self.e_proj, self.f_proj)
                  
    def showsmall(self):
        return '%s|%s|%s|%s|%s|%s|%s|%s|' % (self.name, self.y_pctown, self.y_proj, self.e_proj, self.f_proj,
                                             self.y_vorp, self.e_vorp, self.f_vorp)            
                  
    def project_yahoo(self, scoring):
        self.y_proj = 0.0
        
        self.y_proj += self.y_pass_yds * scoring.pass_yds
        self.y_proj += self.y_pass_yds_300 * scoring.pass_yds_300
        self.y_proj += self.y_pass_yds_400 * scoring.pass_yds_400
        self.y_proj += self.y_pass_td * scoring.pass_td
        self.y_proj += self.y_int_thrown * scoring.int_thrown
        self.y_proj += self.y_rush_yds * scoring.rush_yds
        self.y_proj += self.y_rush_yds_100 * scoring.rush_yds_100
        self.y_proj += self.y_rush_yds_175 * scoring.rush_yds_175
        self.y_proj += self.y_rush_td * scoring.rush_td
        self.y_proj += self.y_reception * scoring.reception
        self.y_proj += self.y_recep_yds * scoring.recep_yds
        self.y_proj += self.y_recep_yds_100 * scoring.recep_yds_100
        self.y_proj += self.y_recep_yds_175 * scoring.recep_yds_175
        self.y_proj += self.y_recep_td * scoring.recep_td
        self.y_proj += self.y_twopt_conv * scoring.twopt_conv
        self.y_proj += self.y_fumble_lost * scoring.fumble_lost
        self.y_proj += self.y_off_fumble_ret_td * scoring.off_fumble_ret_td
        self.y_proj += self.y_pick_six_thrown * scoring.pick_six_thrown
        self.y_proj += self.y_fg_19 * scoring.fg_19
        self.y_proj += self.y_fg_29 * scoring.fg_29
        self.y_proj += self.y_fg_39 * scoring.fg_39
        self.y_proj += self.y_fg_49 * scoring.fg_49
        self.y_proj += self.y_fg_50 * scoring.fg_50
        self.y_proj += self.y_fgmiss_19 * scoring.fgmiss_19
        self.y_proj += self.y_fgmiss_29 * scoring.fgmiss_29
        self.y_proj += self.y_fgmiss_39 * scoring.fgmiss_39
        self.y_proj += self.y_fgmiss_49 * scoring.fgmiss_49
        self.y_proj += self.y_pat_made * scoring.pat_made
        self.y_proj += self.y_pat_miss * scoring.pat_miss
        self.y_proj += self.y_sack * scoring.sack
        self.y_proj += self.y_int_recv * scoring.int_recv
        self.y_proj += self.y_fumble_recv * scoring.fumble_recv
        self.y_proj += self.y_def_td * scoring.def_td
        self.y_proj += self.y_def_safety * scoring.def_safety
        self.y_proj += self.y_block_kick * scoring.block_kick
        self.y_proj += self.y_spec_td * scoring.spec_td
        self.y_proj += self.y_ptsallow_0 * scoring.ptsallow_0
        self.y_proj += self.y_ptsallow_6 * scoring.ptsallow_6
        self.y_proj += self.y_ptsallow_13 * scoring.ptsallow_13
        self.y_proj += self.y_ptsallow_20 * scoring.ptsallow_20
        self.y_proj += self.y_ptsallow_27 * scoring.ptsallow_27
        self.y_proj += self.y_ptsallow_34 * scoring.ptsallow_34
        self.y_proj += self.y_ptsallow_35 * scoring.ptsallow_35
        
        self.y_proj += self.y_idp_tack_solo * scoring.idp_tack_solo
        self.y_proj += self.y_idp_tack_assist * scoring.idp_tack_assist
        self.y_proj += self.y_idp_sack * scoring.idp_sack
        self.y_proj += self.y_idp_int * scoring.idp_int
        self.y_proj += self.y_idp_fumble_force * scoring.idp_fumble_force
        self.y_proj += self.y_idp_fumble_recv * scoring.idp_fumble_recv
        self.y_proj += self.y_idp_td * scoring.idp_td 
        self.y_proj += self.y_idp_safety * scoring.idp_safety
        self.y_proj += self.y_idp_block_kick * scoring.idp_block_kick
        