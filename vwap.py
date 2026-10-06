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
        top_list=[]
        positive_score_card=[]
        negative_score_card=[]
        p_dm=[]
        n_dm=[]
        final_n_dm=[]
        final_p_dm=[]
        finalized_n_dm=[]
        fifteenth_data=[]
        fourteenth_data=[]
        prev_high_list=[]
        prev_low_list=[]
        prev_vwap_list=[]
        prev_close_list=[]
        prev_time_list=[]


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


        if len(main_data)<15:
            print('Insufficient data')
            return


        current_highs=high_list[1:15]
        current_high=high_list[:15]

        prev_closes=closing_list[0:14]
        prev_highs=high_list[0:14]
        prev_lows=low_list[0:14]

        current_low=low_list[:15]
        current_lows=low_list[1:15]

        plus_dm=[x-y for x,y in zip(current_highs,prev_highs)]
        negative_dm=[x-y for x,y in zip(prev_lows,current_lows)]


        tr_1=[x-y for x,y in zip(current_high,current_low)]
        tr_2=[x-y for x,y in zip(current_highs,prev_closes)]
        tr_3=[x-y for x,y in zip(current_low,prev_closes)]


        for values in tr_3:
            main=abs(values)
            top_list.append(main)

        for x,y,z in zip(tr_1,tr_2,top_list):
            kj=max(x,y,z)
            finalized_tr_list.append(kj)

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


        sum_of_tr=sum(finalized_tr_list)
        # sum_of_dm_1=sum(final_p_dm)
        # sum_of_dm_2=sum(final_n_dm)

        pre_post_data=[]

        first_data=main_data[15]
        fifteenth_data.append(first_data)

        prev_data=main_data[14]
        fourteenth_data.append(prev_data)


        for data in fifteenth_data:
            high=data['HIGH']
            low=data['LOW']


        for initialize in fourteenth_data:
            initialize_close=initialize['CLOSING_PRICE']


        new_tr_1=high-low
        pre_post_data.append(new_tr_1)

        new_tr_2=abs(high-initialize_close)
        pre_post_data.append(new_tr_2)

        new_tr_3=abs(low-initialize_close)
        pre_post_data.append(new_tr_3)


        finalized_new_tr=max(pre_post_data)

        first_data['VWAP']=sum_of_tr-(sum_of_tr/14)+finalized_new_tr


        with open(r"C:\Users\dasho\vwap_demo_revised_testing.json",'w') as gf:
            json.dump(main_data,gf,indent=4)


        for latest_data in main_data:
            latest_high=latest_data['HIGH']
            latest_low=latest_data['LOW']
            latest_vwap=latest_data['VWAP']
            latest_close=latest_data['CLOSING_PRICE']
            latest_time=latest_data['TIME']
            prev_high_list.append(latest_high)
            prev_close_list.append(latest_close)
            prev_low_list.append(latest_low)
            prev_vwap_list.append(latest_vwap)
            prev_time_list.append(latest_time)

        revised_high_data=prev_high_list[16:]
        
        revised_closed_price=prev_close_list[15:-1]
        revised_low_price=prev_low_list[16:]
        surya=[]
        surya_2=[]
        surya_3=[]
        tr_1_plus=[x-y for x,y in zip(revised_high_data,revised_low_price)]
        tr_2_plus=[x-y for x,y in zip(revised_high_data,revised_closed_price)]
        tr_3_plus=[x-y for x,y in zip(revised_low_price,revised_closed_price)]
        # print(len(tr_1_plus))
        # print(len(tr_2_plus))
        # print(len(tr_3_plus))
        for the_value in tr_2_plus:
            revised_values=abs(the_value)
            surya_2.append(revised_values)

        for val in tr_3_plus:
            revised_va=abs(val)
            surya_3.append(revised_va)
        for a,b,c in zip(tr_1_plus,surya_2,surya_3):
            if a>b and c:
                surya.append(a)
            if b>a and c:
                surya.append(b)
            if c>a and b:
                surya.append(c)

            if a==b and b==c:
                surya.append(a)
            if b==a and a==c:
                surya.append(b)
            if c==a and b==a:
                surya.append(c)


        
        sum_of_dm_1=sum(final_p_dm)
        
        sum_of_dm_2=sum(finalized_n_dm)
        new_positive_score_card=[]
        new_negative_score_card=[]
        again_p_dm=[]
        again_n_dm=[]
        final_again_n_dm=[]
        final_again_p_dm=[]
        again_finalized_n_dm=[]





        again_highs=high_list[16:]
        again_prev_highs=high_list[15:-1]
        again_prev_lows=low_list[15:-1]
        again_current_lows=low_list[16:]
        again_plus_dm=[x-y for x,y in zip(again_highs,again_prev_highs)]
        again_negative_dm=[x-y for x,y in zip(again_prev_lows,again_current_lows)]
        for positive_dm_ in again_plus_dm:
            if positive_dm_>0:
                new_positive_score_card.append(positive_dm_)
            elif positive_dm_<0:
                new_positive_score_card.append(0)


            elif positive_dm_ == 0:
                new_positive_score_card.append(0)

        for  negative_dm_ in again_negative_dm:
            if negative_dm_<0:
                new_negative_score_card.append(negative_dm_)
            elif negative_dm_>0:
                new_negative_score_card.append(0)

            elif negative_dm_ == 0:
                new_negative_score_card.append(0)





        for jk in new_positive_score_card:
            if jk<=0:
                again_p_dm.append(0)


            if jk>0:
                again_p_dm.append(jk)


        for uj in new_negative_score_card:
            if uj>=0:
                again_n_dm.append(0)


            if uj<0:
                again_n_dm.append(uj)


        print(len(again_n_dm))
        print(len(again_p_dm))

        for adx_ in again_n_dm:
            v_=abs(adx_)
            final_again_n_dm.append(v_)


        for x,y in zip(again_p_dm,final_again_n_dm):



            if x>y:
                final_again_p_dm.append(x)

            if x<y:
                final_again_p_dm.append(0)


            if x==y:
                final_again_p_dm.append(x)

            elif y>x:
                again_finalized_n_dm.append(y)

            if y<x:
                again_finalized_n_dm.append(0)


            if y==x:
                again_finalized_n_dm.append(y)



            





        

        # main_vwap_list=[]
        # local_list=[]
        # current=[]
        # prev=[]
        # for elements in main_data[15:]:
        #     main_vwap=elements['VWAP']
        #     main_vwap_list.append(main_vwap)



        # for latest_elements in main_vwap_list:
        #     new_element_index_finder=main_vwap_list.index(latest_elements)


        #     prev_element=new_element_index_finder-1
        #     current_value=main_vwap_list[new_element_index_finder]
        #     current.append(current_value)
        #     prev_value=main_vwap_list[prev_element]

        #     prev.append(prev_value)


        # first_value=current[0]
        # second_value=surya[0]
        # new_smoothed=first_value-(first_value/14)+second_value
        # local_list.append(new_smoothed)      
        # main_data[16]['VWAP'] = new_smoothed  
      


        # fender=main_vwap_list[2:]

        # for index,rounders in enumerate(fender):
        #     x=[x-(x/14)+y for x,y in zip(local_list,surya[1:])]
        #     new_smoothed=x[-1]
        #     local_list.append(new_smoothed)
        #     #local_list.append(x[-1])
        #     main_data[index + 17]['VWAP'] = new_smoothed

        # with open(r"C:\Users\dasho\vwap_demo_revised_testing.json",'w') as gf:
        #     json.dump(main_data,gf,indent=4)




        # main_data[15]['PLUS_DM']=sum_of_dm_1
        # main_data[15]['NEGATIVE_DM']=sum_of_dm_2



        # main_dm_1_list=[]
        # local_list_=[]

        # current_=[]
        # prev_=[]
        # for elements_ in main_data[15:]:
        #     main_dm=elements_['PLUS_DM']
        #     main_dm_1_list.append(main_dm)

        # for latest_elements_ in main_dm_1_list:
        #     new_element_index_finder_=main_dm_1_list.index(latest_elements_)
        #     prev_element_=new_element_index_finder_-1
        #     current_value_=main_dm_1_list[new_element_index_finder_]
        #     current_.append(current_value_)
        #     prev_value_=main_dm_1_list[prev_element_]
        #     prev_.append(prev_value_)



        # first_value_=current_[0]
        # second_value_=












                    







        














            


        












            







            







            



      










                    



                

                









        

 
         
        








            





        


            






    









        
        #print(k)



        # for y,z ,n  in zip(revised_vwap_list,surya,k):
            
        #     x=y-(y/14)+z
        #     n['VWAP']=x
        







        # with open(r"C:\Users\dasho\vwap_demo_revised_testing.json",'w') as se:

           



        #     json.dump(main_data,se,indent=4)


        




                
                
            











            




        


        


        




















        
        









        

     
        







        



        


        






        
       





                    
                
        




        
        


        


       







g=VWAP()
g.getting_the_data()
g.analyzing_the_data()