import requests as rq
import pandas as pd
import csv 
import json 
from datetime import datetime
import time




class VWAP:
    def __init__(self):
        pass






    def getting_the_data(self):
        with open(r"C:\Users\dasho\vwap_demo_revised_testing.json",'r') as df:
            data=json.load(df)
            return data 




    def analyzing_the_data(self):
        main_data=self.getting_the_data()
        current_date="2026-09-28"
        for datas in main_data:
            opening_prices=datas['OPEN']
            closing_prices=datas['CLOSING_PRICE']
            high_prices=datas['HIGH']
            low_prices=datas['LOW']
            dates=datas['DATE']
            vols=datas['VOLUME']
            if current_date==dates:
                vwap_calc=high_prices+low_prices+closing_prices//3
                vwap_vol=vwap_calc*vols
                datas['VWAP_CU']=vwap_vol
        with open(r"C:\Users\dasho\vwap_demo_revised_testing.json",'w') as gf:
            json.dump(main_data,gf,indent=4)



        total_sum=[]
        vol_total=[]
        first_14_data_list=[]
        closing_list=[]
        opening_list=[]
        high_list=[]
        low_list=[]
        date_list=[]
        time_list=[]
        finalized_tr_list=[]

        for revised_data in main_data:
            revised_close=revised_data['CLOSING_PRICE']
            revised_open=revised_data['OPEN']
            revised_dates=revised_data['DATE']
            revised_high=revised_data['HIGH']
            revised_low=revised_data['LOW']
            revised_time=revised_data['TIME']
            revised_volume=revised_data['VOLUME']
            cumulative_volume=revised_data['VWAP_CU']
            if current_date==revised_dates:
                closing_list.append(revised_close)
                opening_list.append(revised_open)
                high_list.append(revised_high)
                low_list.append(revised_low)
                time_list.append(revised_time)
                total_sum.append(cumulative_volume)
                vol_total.append(revised_volume)


        final_data=sum(total_sum)
        final_vols=sum(vol_total)
        final_result=final_data//final_vols



       
        if len(main_data)<14:
            print('Insufficient data')
            return



        # prev_time_list=[]
        # prev_close_list=[]
        # #print(closing_list)
        # for prices in time_list:
        #     index_finder=time_list.index(prices)
        #     if index_finder%2!=0:

        #         prev_time_list.append(index_finder)
        # #print(prev_time_list)
        # for price in prev_time_list:
        #     prev_closings=closing_list[price]
        #     #print(prev_closings)
        #     prev_close_list.append(prev_closings)
      
        current_highs=high_list[1:14]
        current_high=high_list[:14]

        prev_closes=closing_list[0:13]
        prev_highs=high_list[0:13]
        prev_lows=low_list[0:13]

        current_low=low_list[:14]
        current_lows=low_list[1:14]

        plus_dm=[x-y for x,y in zip(current_highs,prev_highs)]
        negative_dm=[x-y for x,y in zip(prev_lows,current_lows)]




        tr_1=[x-y for x,y in zip(current_high,current_low)]
        tr_2=[x-y for x,y in zip(current_highs,prev_closes)]
        tr_3=[x-y for x,y in zip(current_low,prev_closes)]
        top_list=[]
        for values in tr_3:
            main=abs(values)
            top_list.append(main)
        for x,y,z in zip(tr_1,tr_2,top_list):
            kj=max(x,y,z)
            finalized_tr_list.append(kj)


        # print(plus_dm)
        # print(negative_dm)
        positive_score_card=[]
        negative_score_card=[]
        p_dm=[]
        n_dm=[]
        final_n_dm=[]


        for positive_dm in plus_dm:
            if positive_dm>0:
                positive_score_card.append(positive_dm)

            elif positive_dm<0:
                positive_score_card.append(0)
        for negative_dms in negative_dm:
            if negative_dms<0:
                negative_score_card.append(negative_dms)
            if negative_dms>0:
                negative_score_card.append(0)


        # print(len(positive_score_card))
        # print(len(negative_score_card))



        for kj in positive_score_card:
            if kj<=0:
                p_dm.append(0)
            if kj>0:
                p_dm.append(kj)
        for ju in negative_score_card:
            if ju>=0:
                n_dm.append(0)
            if ju<0:
                n_dm.append(ju)

        print(p_dm)
        final_p_dm=[]
        finalized_n_dm=[]


        for adx_based in n_dm:
            v=abs(adx_based)
            final_n_dm.append(v)

        for x,y in zip(p_dm,final_n_dm):
            if x>y:
                final_p_dm.append(x)
            if x<y:
                final_p_dm.append(0)
            if x==y:
                final_p_dm.append(x)

            elif y>x:
                finalized_n_dm.append(y)
            if y<x:
                finalized_n_dm.append(0)
            if y==x:
                finalized_n_dm.append(y)
        print(final_p_dm)
        
        print(finalized_n_dm)





                    
                
        




        
        


        


       







g=VWAP()
g.getting_the_data()
g.analyzing_the_data()