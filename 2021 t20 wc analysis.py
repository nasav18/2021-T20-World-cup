import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

t20wc=pd.read_csv(r'C:\Users\girie\Downloads\t20wc (1).csv')
nz_t20wc=t20wc.loc[t20wc['Team'] == 'New Zealand Innings']
aus_t20wc=t20wc.loc[t20wc['Team'] == 'Australia Innings']
"""train['Winner']=train['Winner'].str.replace('\d+', '')
train['Winner']=train['Winner'].str.replace('runs', '')
train['Winner']=train['Winner'].str.replace('wkts', '')
train['Winner']=train['Winner'].str.replace('by', '')"""

t20i=pd.read_csv(r'C:\Users\girie\Downloads\t20i.csv')
aus_t20i=t20i.loc[t20i['Team']=='Australia']


innings_1=aus_t20i.loc[aus_t20i['Inns'] == 1]
innings_1_win=innings_1.loc[innings_1['Result'] == 'won']
innings_2=aus_t20i.loc[aus_t20i['Inns'] == 2]
innings_2_win=innings_2.loc[innings_2['Result'] == 'won']
#innings_1_win=len(eng_t20i.loc[eng_t20i['Winner'] == 'England won by*'])


men_t20i_stats=pd.read_csv(r'C:\Users\girie\Downloads\Men T20I STATS.csv')
aus_men_t20i=men_t20i_stats.loc[men_t20i_stats['Country'] == 'Australia']
aus_v_nz_men=aus_men_t20i.loc[aus_men_t20i['Opposition'] == 'v New Zealand']
ausvnz_final=aus_v_nz_men.drop_duplicates()
players=aus_men_t20i['Innings Player'].unique()

dwarner=ausvnz_final.loc[ausvnz_final['Innings Player']=='JP Behrendorff']
dwarner_runs=dwarner['Innings Runs Scored']

#jbuttler=engvnz_final.loc[engvnz_final['Innings Player']=='JC Buttler']
#jroy=engvnz_final.loc[engvnz_final['Innings Player']=='JJ Roy']
#jbarry=engvnz_final.loc[engvnz_final['Innings Player']=='JM Bairstow']

#tcurran=engvnz_final.loc[engvnz_final['Innings Player']=='DJ Malan']

#emorgan=emorgan.fillna(0)
#emorgan_runs=emorgan['Innings Runs Scored Num']


balls_faced=ausvnz_final.loc[ausvnz_final['Innings Balls Faced'] > '10']
#engvnz_final.to_csv('engvnz_final.csv')
#emorgan_runs=emorgan.loc[emorgan['Innings Runs Scored']]
#RG_Sharma=indvnz_final.loc[indvnz_final['Innings Player']=='RG Sharma'] 
#indvnz_final=indvnz_final.fillna(0)
#strike_rate=indvnz_final.loc[indvnz_final['Innings Batting Strike Rate'] > '0.00']"""
