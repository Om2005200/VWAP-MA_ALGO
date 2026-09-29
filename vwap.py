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



        prev_time_list=[]
        #print(closing_list)
        for prices in time_list:
            index_finder=time_list.index(prices)
            if index_finder%2!=0:

                prev_time_list.append(index_finder)
        print(prev_time_list)
        for price in prev_time_list:
            prev_closings=closing_list[price]
            print(prev_closings)


            

        for_closes=closing_list[:14]
        for_opens=opening_list[:14]
        for_highs=high_list[:14]
        for_lows=low_list[:14]
        


        


       







g=VWAP()
g.getting_the_data()
g.analyzing_the_data()