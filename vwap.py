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
        file_list=["360one_revised_dataset_rsi_pro_data.json", "abb_revised_dataset_rsi_pro_data.json", "aplapollo_revised_dataset_rsi_pro_data.json", "aubank_revised_dataset_rsi_pro_data.json", "adaniensol_revised_dataset_rsi_pro_data.json", "adanient_revised_dataset_rsi_pro_data.json", "adanigreen_revised_dataset_rsi_pro_data.json", "adaniports_revised_dataset_rsi_pro_data.json", "adanipower_revised_dataset_rsi_pro_data.json", "atgl_revised_dataset_rsi_pro_data.json", "abcapital_revised_dataset_rsi_pro_data.json", "alkem_revised_dataset_rsi_pro_data.json", "ambujacem_revised_dataset_rsi_pro_data.json", "apollohosp_revised_dataset_rsi_pro_data.json", "ashokley_revised_dataset_rsi_pro_data.json", "asianpaint_revised_dataset_rsi_pro_data.json", "astral_revised_dataset_rsi_pro_data.json", "auropharma_revised_dataset_rsi_pro_data.json", "dmart_revised_dataset_rsi_pro_data.json", "axisbank_revised_dataset_rsi_pro_data.json", "bse_revised_dataset_rsi_pro_data.json", "bajaj-auto_revised_dataset_rsi_pro_data.json", "bajfinance_revised_dataset_rsi_pro_data.json", "bajajfinsv_revised_dataset_rsi_pro_data.json", "bajajhldng_revised_dataset_rsi_pro_data.json", "bankbaroda_revised_dataset_rsi_pro_data.json", "bankindia_revised_dataset_rsi_pro_data.json", "bdl_revised_dataset_rsi_pro_data.json", "bel_revised_dataset_rsi_pro_data.json", "bharatforg_revised_dataset_rsi_pro_data.json", "bhel_revised_dataset_rsi_pro_data.json", "bpcl_revised_dataset_rsi_pro_data.json", "bhartiartl_revised_dataset_rsi_pro_data.json", "groww_revised_dataset_rsi_pro_data.json", "biocon_revised_dataset_rsi_pro_data.json", "bluestarco_revised_dataset_rsi_pro_data.json", "boschltd_revised_dataset_rsi_pro_data.json", "britannia_revised_dataset_rsi_pro_data.json", "cgpower_revised_dataset_rsi_pro_data.json", "canbk_revised_dataset_rsi_pro_data.json", "cholafin_revised_dataset_rsi_pro_data.json", "cipla_revised_dataset_rsi_pro_data.json", "coalindia_revised_dataset_rsi_pro_data.json", "cochinship_revised_dataset_rsi_pro_data.json", "coforge_revised_dataset_rsi_pro_data.json", "colpal_revised_dataset_rsi_pro_data.json", "concor_revised_dataset_rsi_pro_data.json", "coromandel_revised_dataset_rsi_pro_data.json", "cumminsind_revised_dataset_rsi_pro_data.json", "dlf_revised_dataset_rsi_pro_data.json", "dabur_revised_dataset_rsi_pro_data.json", "divislab_revised_dataset_rsi_pro_data.json", "dixon_revised_dataset_rsi_pro_data.json", "drreddy_revised_dataset_rsi_pro_data.json", "eichermot_revised_dataset_rsi_pro_data.json", "eternal_revised_dataset_rsi_pro_data.json", "exideind_revised_dataset_rsi_pro_data.json", "nykaa_revised_dataset_rsi_pro_data.json", "federalbnk_revised_dataset_rsi_pro_data.json", "fortis_revised_dataset_rsi_pro_data.json", "gail_revised_dataset_rsi_pro_data.json", "gvt&d_revised_dataset_rsi_pro_data.json", "gmrairport_revised_dataset_rsi_pro_data.json", "glenmark_revised_dataset_rsi_pro_data.json", "godfryphlp_revised_dataset_rsi_pro_data.json", "godrejcp_revised_dataset_rsi_pro_data.json", "godrejprop_revised_dataset_rsi_pro_data.json", "grasim_revised_dataset_rsi_pro_data.json", "hcltech_revised_dataset_rsi_pro_data.json", "hdfcamc_revised_dataset_rsi_pro_data.json", "hdfcbank_revised_dataset_rsi_pro_data.json", "hdfclife_revised_dataset_rsi_pro_data.json", "havells_revised_dataset_rsi_pro_data.json", "heromotoco_revised_dataset_rsi_pro_data.json", "hindalco_revised_dataset_rsi_pro_data.json", "hal_revised_dataset_rsi_pro_data.json", "hindpetro_revised_dataset_rsi_pro_data.json", "hindunilvr_revised_dataset_rsi_pro_data.json", "hindzinc_revised_dataset_rsi_pro_data.json", "powerindia_revised_dataset_rsi_pro_data.json", "hudco_revised_dataset_rsi_pro_data.json", "hyundai_revised_dataset_rsi_pro_data.json", "icicibank_revised_dataset_rsi_pro_data.json", "icicigi_revised_dataset_rsi_pro_data.json", "iciciamc_revised_dataset_rsi_pro_data.json", "idfcfirstb_revised_dataset_rsi_pro_data.json", "itc_revised_dataset_rsi_pro_data.json", "indianb_revised_dataset_rsi_pro_data.json", "indhotel_revised_dataset_rsi_pro_data.json", "ioc_revised_dataset_rsi_pro_data.json", "irctc_revised_dataset_rsi_pro_data.json", "irfc_revised_dataset_rsi_pro_data.json", "ireda_revised_dataset_rsi_pro_data.json", "industower_revised_dataset_rsi_pro_data.json", "indusindbk_revised_dataset_rsi_pro_data.json", "naukri_revised_dataset_rsi_pro_data.json", "infy_revised_dataset_rsi_pro_data.json", "indigo_revised_dataset_rsi_pro_data.json", "jswenergy_revised_dataset_rsi_pro_data.json", "jswsteel_revised_dataset_rsi_pro_data.json", "jindalstel_revised_dataset_rsi_pro_data.json", "jiofin_revised_dataset_rsi_pro_data.json", "jublfood_revised_dataset_rsi_pro_data.json", "kei_revised_dataset_rsi_pro_data.json", "kpittech_revised_dataset_rsi_pro_data.json", "kalyankjil_revised_dataset_rsi_pro_data.json", "kotakbank_revised_dataset_rsi_pro_data.json", "ltf_revised_dataset_rsi_pro_data.json", "lgeindia_revised_dataset_rsi_pro_data.json", "lichsgfin_revised_dataset_rsi_pro_data.json", "ltm_revised_dataset_rsi_pro_data.json", "lt_revised_dataset_rsi_pro_data.json", "lauruslabs_revised_dataset_rsi_pro_data.json", "lenskart_revised_dataset_rsi_pro_data.json", "lodha_revised_dataset_rsi_pro_data.json", "lupin_revised_dataset_rsi_pro_data.json", "mrf_revised_dataset_rsi_pro_data.json", "m&mfin_revised_dataset_rsi_pro_data.json", "m&m_revised_dataset_rsi_pro_data.json", "mankind_revised_dataset_rsi_pro_data.json", "marico_revised_dataset_rsi_pro_data.json", "maruti_revised_dataset_rsi_pro_data.json", "mfsl_revised_dataset_rsi_pro_data.json", "maxhealth_revised_dataset_rsi_pro_data.json", "mazdock_revised_dataset_rsi_pro_data.json", "motilalofs_revised_dataset_rsi_pro_data.json", "mphasis_revised_dataset_rsi_pro_data.json", "mcx_revised_dataset_rsi_pro_data.json", "muthootfin_revised_dataset_rsi_pro_data.json", "nhpc_revised_dataset_rsi_pro_data.json", "nmdc_revised_dataset_rsi_pro_data.json", "ntpc_revised_dataset_rsi_pro_data.json", "nationalum_revised_dataset_rsi_pro_data.json", "nestleind_revised_dataset_rsi_pro_data.json", "oberoirlty_revised_dataset_rsi_pro_data.json", "ongc_revised_dataset_rsi_pro_data.json", "oil_revised_dataset_rsi_pro_data.json", "paytm_revised_dataset_rsi_pro_data.json", "ofss_revised_dataset_rsi_pro_data.json", "policybzr_revised_dataset_rsi_pro_data.json", "piind_revised_dataset_rsi_pro_data.json", "pageind_revised_dataset_rsi_pro_data.json", "patanjali_revised_dataset_rsi_pro_data.json", "persistent_revised_dataset_rsi_pro_data.json", "phoenixltd_revised_dataset_rsi_pro_data.json", "pidilitind_revised_dataset_rsi_pro_data.json", "polycab_revised_dataset_rsi_pro_data.json", "pfc_revised_dataset_rsi_pro_data.json", "powergrid_revised_dataset_rsi_pro_data.json", "premierene_revised_dataset_rsi_pro_data.json", "prestige_revised_dataset_rsi_pro_data.json", "pnb_revised_dataset_rsi_pro_data.json", "recltd_revised_dataset_rsi_pro_data.json", "radico_revised_dataset_rsi_pro_data.json", "rvnl_revised_dataset_rsi_pro_data.json", "reliance_revised_dataset_rsi_pro_data.json", "sbicard_revised_dataset_rsi_pro_data.json", "sbilife_revised_dataset_rsi_pro_data.json", "srf_revised_dataset_rsi_pro_data.json", "motherson_revised_dataset_rsi_pro_data.json", "shreecem_revised_dataset_rsi_pro_data.json", "shriramfin_revised_dataset_rsi_pro_data.json", "enrin_revised_dataset_rsi_pro_data.json", "siemens_revised_dataset_rsi_pro_data.json", "solarinds_revised_dataset_rsi_pro_data.json", "sbin_revised_dataset_rsi_pro_data.json", "sail_revised_dataset_rsi_pro_data.json", "sunpharma_revised_dataset_rsi_pro_data.json", "supremeind_revised_dataset_rsi_pro_data.json", "suzlon_revised_dataset_rsi_pro_data.json", "swiggy_revised_dataset_rsi_pro_data.json", "tvsmotor_revised_dataset_rsi_pro_data.json", "tatacap_revised_dataset_rsi_pro_data.json", "tatacomm_revised_dataset_rsi_pro_data.json", "tcs_revised_dataset_rsi_pro_data.json", "tataconsum_revised_dataset_rsi_pro_data.json", "tataelxsi_revised_dataset_rsi_pro_data.json", "tatainvest_revised_dataset_rsi_pro_data.json", "tmcv_revised_dataset_rsi_pro_data.json", "tmpv_revised_dataset_rsi_pro_data.json", "tatapower_revised_dataset_rsi_pro_data.json", "tatasteel_revised_dataset_rsi_pro_data.json", "techm_revised_dataset_rsi_pro_data.json", "titan_revised_dataset_rsi_pro_data.json", "torntpharm_revised_dataset_rsi_pro_data.json", "trent_revised_dataset_rsi_pro_data.json", "tiindia_revised_dataset_rsi_pro_data.json", "upl_revised_dataset_rsi_pro_data.json", "ultracemco_revised_dataset_rsi_pro_data.json", "unionbank_revised_dataset_rsi_pro_data.json", "unitdspr_revised_dataset_rsi_pro_data.json", "vbl_revised_dataset_rsi_pro_data.json", "vedl_revised_dataset_rsi_pro_data.json", "vmm_revised_dataset_rsi_pro_data.json", "idea_revised_dataset_rsi_pro_data.json", "voltas_revised_dataset_rsi_pro_data.json", "waareeener_revised_dataset_rsi_pro_data.json", "wipro_revised_dataset_rsi_pro_data.json", "yesbank_revised_dataset_rsi_pro_data.json", "zyduslife_revised_dataset_rsi_pro_data.json"]

        #file_list = ["abb_revised_dataset_rsi_pro_data.json", "adaniensol_revised_dataset_rsi_pro_data.json", "adanient_revised_dataset_rsi_pro_data.json", "adanigreen_revised_dataset_rsi_pro_data.json", "adaniports_revised_dataset_rsi_pro_data.json", "adanipower_revised_dataset_rsi_pro_data.json", "ambujacem_revised_dataset_rsi_pro_data.json", "apollohosp_revised_dataset_rsi_pro_data.json", "asianpaint_revised_dataset_rsi_pro_data.json", "dmart_revised_dataset_rsi_pro_data.json", "axisbank_revised_dataset_rsi_pro_data.json", "bajaj-auto_revised_dataset_rsi_pro_data.json", "bajfinance_revised_dataset_rsi_pro_data.json", "bajajfinsv_revised_dataset_rsi_pro_data.json", "bajajhldng_revised_dataset_rsi_pro_data.json", "bankbaroda_revised_dataset_rsi_pro_data.json", "bel_revised_dataset_rsi_pro_data.json", "bpcl_revised_dataset_rsi_pro_data.json", "bhartiartl_revised_dataset_rsi_pro_data.json", "boschltd_revised_dataset_rsi_pro_data.json", "britannia_revised_dataset_rsi_pro_data.json", "cgpower_revised_dataset_rsi_pro_data.json", "canbk_revised_dataset_rsi_pro_data.json", "cholafin_revised_dataset_rsi_pro_data.json", "cipla_revised_dataset_rsi_pro_data.json", "coalindia_revised_dataset_rsi_pro_data.json", "cumminsind_revised_dataset_rsi_pro_data.json", "dlf_revised_dataset_rsi_pro_data.json", "divislab_revised_dataset_rsi_pro_data.json", "drreddy_revised_dataset_rsi_pro_data.json", "eichermot_revised_dataset_rsi_pro_data.json", "eternal_revised_dataset_rsi_pro_data.json", "gail_revised_dataset_rsi_pro_data.json", "godrejcp_revised_dataset_rsi_pro_data.json", "grasim_revised_dataset_rsi_pro_data.json", "hcltech_revised_dataset_rsi_pro_data.json", "hdfcamc_revised_dataset_rsi_pro_data.json", "hdfcbank_revised_dataset_rsi_pro_data.json", "hdfclife_revised_dataset_rsi_pro_data.json", "hindalco_revised_dataset_rsi_pro_data.json", "hal_revised_dataset_rsi_pro_data.json", "hindunilvr_revised_dataset_rsi_pro_data.json", "hindzinc_revised_dataset_rsi_pro_data.json", "hyundai_revised_dataset_rsi_pro_data.json", "icicibank_revised_dataset_rsi_pro_data.json", "itc_revised_dataset_rsi_pro_data.json", "indhotel_revised_dataset_rsi_pro_data.json", "ioc_revised_dataset_rsi_pro_data.json", "irfc_revised_dataset_rsi_pro_data.json", "infy_revised_dataset_rsi_pro_data.json", "indigo_revised_dataset_rsi_pro_data.json", "jswsteel_revised_dataset_rsi_pro_data.json", "jindalstel_revised_dataset_rsi_pro_data.json", "jiofin_revised_dataset_rsi_pro_data.json", "kotakbank_revised_dataset_rsi_pro_data.json", "ltm_revised_dataset_rsi_pro_data.json", "lt_revised_dataset_rsi_pro_data.json", "lodha_revised_dataset_rsi_pro_data.json", "m&m_revised_dataset_rsi_pro_data.json", "maruti_revised_dataset_rsi_pro_data.json", "maxhealth_revised_dataset_rsi_pro_data.json", "mazdock_revised_dataset_rsi_pro_data.json", "muthootfin_revised_dataset_rsi_pro_data.json", "ntpc_revised_dataset_rsi_pro_data.json", "nestleind_revised_dataset_rsi_pro_data.json", "ongc_revised_dataset_rsi_pro_data.json", "pidilitind_revised_dataset_rsi_pro_data.json", "pfc_revised_dataset_rsi_pro_data.json", "powergrid_revised_dataset_rsi_pro_data.json", "pnb_revised_dataset_rsi_pro_data.json", "recltd_revised_dataset_rsi_pro_data.json", "reliance_revised_dataset_rsi_pro_data.json", "sbilife_revised_dataset_rsi_pro_data.json", "motherson_revised_dataset_rsi_pro_data.json", "shreecem_revised_dataset_rsi_pro_data.json", "shriramfin_revised_dataset_rsi_pro_data.json", "enrin_revised_dataset_rsi_pro_data.json", "siemens_revised_dataset_rsi_pro_data.json", "solarinds_revised_dataset_rsi_pro_data.json", "sbin_revised_dataset_rsi_pro_data.json", "sunpharma_revised_dataset_rsi_pro_data.json", "tvsmotor_revised_dataset_rsi_pro_data.json", "tatacap_revised_dataset_rsi_pro_data.json", "tcs_revised_dataset_rsi_pro_data.json", "tataconsum_revised_dataset_rsi_pro_data.json", "tmcv_revised_dataset_rsi_pro_data.json", "tmpv_revised_dataset_rsi_pro_data.json", "tatapower_revised_dataset_rsi_pro_data.json", "tatasteel_revised_dataset_rsi_pro_data.json", "techm_revised_dataset_rsi_pro_data.json", "titan_revised_dataset_rsi_pro_data.json", "torntpharm_revised_dataset_rsi_pro_data.json", "trent_revised_dataset_rsi_pro_data.json", "ultracemco_revised_dataset_rsi_pro_data.json", "unionbank_revised_dataset_rsi_pro_data.json", "unitdspr_revised_dataset_rsi_pro_data.json", "vbl_revised_dataset_rsi_pro_data.json", "vedl_revised_dataset_rsi_pro_data.json", "wipro_revised_dataset_rsi_pro_data.json", "zyduslife_revised_dataset_rsi_pro_data.json"]
        
        all_data=[]
        for files in file_list:
            with open(r"C:\Users\dasho\{}".format(files),'r') as k:
                data=json.load(k)
            all_data.append((data,files))

        return all_data

    
       
    def opening_the_order_log(self,file_name):

        file_path = r'C:\Users\dasho\{}vwap_strategy_orderbook.json'.format(file_name)


        try:
            with open(file_path, 'r') as x:
                data = json.load(x)

                # if file somehow contains null
                if data is None:
                    data = []

                return data

        except FileNotFoundError:

            print("NO ORDERBOOK FOUND. CREATING NEW FILE")

            with open(file_path, 'w') as x:
                json.dump([], x, indent=4)

            return []

        except json.JSONDecodeError:

            print("ORDERBOOK CORRUPTED. RESETTING")

            with open(file_path, 'w') as x:
                json.dump([], x, indent=4)

            return []

    def analyzing_the_data(self,stock_data:str):
        main_data,file_name=stock_data
        current_date="2026-09-28"
        order_log=self.opening_the_order_log(file_name)


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

        with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as gf:
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
        semi_top_list=[]


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


        for va in tr_2:
            main_=abs(va)
            semi_top_list.append(main_)
            

        for x,y,z in zip(tr_1,semi_top_list,top_list):
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

        first_data['VWAP']=sum_of_tr


        with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as gf:
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



        # print(len(again_finalized_n_dm))
        # print(len(final_again_p_dm))





        

        main_vwap_list=[]
        local_list=[]
        current=[]
        prev=[]
        for elements in main_data[15:]:
            main_vwap=elements['VWAP']
            main_vwap_list.append(main_vwap)



        for latest_elements in main_vwap_list:
            new_element_index_finder=main_vwap_list.index(latest_elements)


            prev_element=new_element_index_finder-1
            current_value=main_vwap_list[new_element_index_finder]
            current.append(current_value)
            prev_value=main_vwap_list[prev_element]

            prev.append(prev_value)


        first_value=current[0]
        second_value=surya[0]
        new_smoothed=first_value-(first_value/14)+second_value
        local_list.append(new_smoothed)      
        main_data[16]['VWAP'] = new_smoothed  
      


        fender=main_vwap_list[2:]

        for index,rounders in enumerate(fender):
            x=[x-(x/14)+y for x,y in zip(local_list,surya[1:])]
            new_smoothed=x[-1]
            local_list.append(new_smoothed)
            #local_list.append(x[-1])
            main_data[index + 17]['VWAP'] = new_smoothed

        with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as gf:
            json.dump(main_data,gf,indent=4)




        main_data[15]['PLUS_DM']=sum_of_dm_1

        main_data[15]['NEGATIVE_DM']=sum_of_dm_2
        with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as lk:
            json.dump(main_data,lk,indent=4)




        ######## POSITIVE DM ########



        main_dm_positive_list=[]
        localised_list=[]
        current_list=[]
        previous_list=[]


        for atoms in main_data[15:]:
            main_dm_plus=atoms['PLUS_DM']
            main_dm_positive_list.append(main_dm_plus)
        for latest_atoms in main_dm_positive_list:
            latest_element_index_finder=main_dm_positive_list.index(latest_atoms)
            prev_elements=latest_element_index_finder-1
            current_value_=main_dm_positive_list[latest_element_index_finder]
            current_list.append(current_value_)
            prev_value_=main_dm_positive_list[prev_elements]
            previous_list.append(prev_value_)



        first_value_=current_list[0]
        second_value_=final_again_p_dm[0]
        new_smoothed_dm_positive=first_value_-(first_value_/14)+second_value_
        localised_list.append(new_smoothed_dm_positive)

        main_data[16]['PLUS_DM']=new_smoothed_dm_positive
        
        with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as oy:
            json.dump(main_data,oy,indent=4)

        fender_=main_dm_positive_list[2:]
        for index,rounders_ in enumerate(fender_):
            x=[x-(x/14)+y for x,y in zip(localised_list,final_again_p_dm[1:])]
            new_smoothed_final=x[-1]
            main_data[index+17]['PLUS_DM']=new_smoothed_final

        with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as hy:
            json.dump(main_data,hy,indent=4)




        main_dm_negative_list=[]
        localised_list_negative=[]
        current_list_=[]
        previous_list_=[]
        dx_list=[]


        for tr in main_data[15:]:
            main_dm_negative=tr['NEGATIVE_DM']
            main_dm_negative_list.append(main_dm_negative)
        for latest_tr in main_dm_negative_list:
            latest_element_index_finder_negative=main_dm_negative_list.index(latest_tr)
            prev_elements_=latest_element_index_finder_negative-1
            current_value_ne=main_dm_negative_list[latest_element_index_finder_negative]
            current_list_.append(current_value_ne)
            prev_value_ne=main_dm_negative_list[prev_elements_]

        first_value_n=current_list_[0]
        second_value_n=again_finalized_n_dm[0]
        new_smoothed_dm_negative=first_value_n-(first_value_n/14)+second_value_n
        localised_list_negative.append(new_smoothed_dm_negative)
        main_data[16]['NEGATIVE_DM']=new_smoothed_dm_negative
        with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as iu:
            json.dump(main_data,iu,indent=4)


        fender_ne=main_dm_negative_list[2:]
        for index,rounder in enumerate(fender_ne):
            x=[x-(x/14)+y for x,y in zip(localised_list_negative,again_finalized_n_dm)]
            new_smoothed_final_=x[-1]
            main_data[index+17]['NEGATIVE_DM']=new_smoothed_final_
        with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as uu:
            json.dump(main_data,uu,indent=4)



        for again_ in main_data:
            smoothed_dm=again_['PLUS_DM']
            smoothed_tr=again_['VWAP']
            negative_dm=again_['NEGATIVE_DM']

            di=(smoothed_dm/smoothed_tr)*100
            di_n=(negative_dm/smoothed_tr)*100
            again_['DI_NEGATIVE']=di_n
            
            with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as uy:
                json.dump(main_data,uy,indent=4)

                            

            again_['DI_PLUS']=di

          
            with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as uy:
                json.dump(main_data,uy,indent=4)


            new_di_plus=again_['DI_PLUS']
            new_di_negative=again_['DI_NEGATIVE']
            
            dx=abs((new_di_plus-(-new_di_negative))/new_di_plus+(-new_di_negative))*100
            again_['DX']=dx
            with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as re:
                json.dump(main_data,re,indent=4)

        
        for ltx in main_data:
            new_dx_values=ltx['DX']
            dx_list.append(new_dx_values)

        first_14_dx_value=sum(dx_list[:14])/14


        main_data[15]['ADX']=first_14_dx_value
        with open(r'C:\Users\dasho\{}.json'.format(file_name),'w')as ww:
            json.dump(main_data,ww,indent=4)




        main_adx_list=[]
        local_list_adx=[]
        current_adx_list=[]
        previous_adx_list=[]



        for jag in main_data[15:]:
            main_adx=jag['ADX']
            main_adx_list.append(main_adx)

        for latest_ in main_adx_list:
            latest_element_index_finder_adx=main_adx_list.index(latest_)
            prev_element_adx=latest_element_index_finder_adx-1
            current_adx=main_adx_list[latest_element_index_finder_adx]
            current_adx_list.append(current_adx)
            prev_value_adx=main_adx_list[prev_element_adx]
            previous_adx_list.append(prev_value_adx)





        first_adx_value=current_adx_list[0]
        second_adx_value=dx_list[0]
        new_adx_value=((first_adx_value*13)+second_adx_value)/14
        local_list_adx.append(new_adx_value)

        main_data[16]['ADX']=new_adx_value
        with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as te:
            json.dump(main_data,te,indent=4)



        fender_adx=main_adx_list[2:]



        for index,rounde in enumerate(fender_adx):
            x=[x-(x/14)+y for x,y in zip(local_list_adx,dx_list[1:])]
            new_smoothed_adx=x[-1]
            local_list_adx.append(new_smoothed_adx)
            main_data[index+17]['ADX']=new_smoothed_adx

        with open(r'C:\Users\dasho\{}.json'.format(file_name),'w') as ll:
            json.dump(main_data,ll,indent=4)




    def taking_the_positions(self,stock_data:str):




        main_data,file_name=stock_data
        order_log=self.opening_the_order_log(file_name)
        close_list=[]
        time_list=[]



        current_date="2026-09-28"

        for datas in main_data:
            main_close=datas['CLOSING_PRICE']
            main_open=datas['OPEN']
            main_time=datas['TIME']
            #main_rsi=datas['RSI']
            main_vwap=datas['VWAP']
            main_di_plus=datas['DI_PLUS']
            main_date=datas['DATE']
            main_di_negative=datas['DI_NEGATIVE']

            close_list.append(main_close)
            time_list.append(main_time)


        current_closing=close_list[-1]
        current_time=time_list[-1]
        print(current_time)

        for fle in main_data:
            fle_close=fle['CLOSING_PRICE']
            fle_open=fle['OPEN']
            fle_date=fle['DATE']
            if current_date==fle_date:
                if fle_close==current_closing:
                    if fle_close>fle_open:


                        semi_green_candle=[]
                        finalized_green_candle=[]
                        for green_data in main_data:
                            green_close=green_data['CLOSING_PRICE']
                            green_open=green_data['OPEN']
                            green_time=green_data['TIME']
                            green_vwap=green_data['VWAP']
                            green_date=green_data['DATE']

                            green_di_plus=green_data['DI_PLUS']
                            green_di_negative=green_data['DI_NEGATIVE']


                            if green_date==current_date:
                                if green_close==current_closing:

                                    if green_close>green_open:
                                        
                                        if green_time==current_time:
                                            if green_close>green_vwap:
                                                if green_di_plus<green_di_negative:

                                                
                                                    semi_green_candle.append(green_data)
                                                    main_green_candle=semi_green_candle[-1]


                        if main_green_candle is not None:
                            finalized_green_candle.append(main_green_candle)


                            print(f"\n[{file_name}] ✅ COMPLETE SETUP APPROVED")
                            print(f"[{file_name}] CANDLE : {semi_green_candle}")
                            
                            if new_order not in order_log:

                                order_log.append(new_order)

                                with open(r'C:\Users\dasho\{}vwap_strategy_orderbook.json'.format(file_name),'w') as rr:
                                    json.dump(order_log,rr,indent=4)

                    elif fle_close<fle_open:
                        semi_red_candle_list=[]
                        finalized_red_candle=[]
                        semi_red_candle=None

                        for red_candles in main_data:
                            red_close=red_candles['CLOSE']
                            red_opens=red_candles['OPEN']
                            red_dates=red_candles['DATE']
                            red_vwap=red_candles['VWAP']
                            red_di_plus=red_candles['DI_PLUS']
                            red_time=red_candles['TIME']

                            red_di_negative=red_candles['DI_NEGATIVE']


                            if current_date==red_dates:
                                if red_close==current_closing:
                                    if red_time==current_time:
                                        if red_close<red_opens:
                                            if red_di_negative>red_di_plus:


                                                semi_red_candle_list.append(red_candles)
                                                semi_red_candle=semi_red_candle_list[-1]



                        if semi_red_candle is not None:
                            finalized_red_candle.append(semi_red_candle)



                            new_order={
                                'STATUS':'OPEN',
                                'CANDLE_':semi_red_candle
                            }


                            print(f"\n[{file_name}] ✅ COMPLETE SETUP APPROVED")
                            print(f"[{file_name}] CANDLE : {semi_red_candle}")
                            
                            if new_order not in order_log:

                                order_log.append(new_order)

                                with open(r'C:\Users\dasho\{}vwap_strategy_orderbook.json'.format(file_name),'w') as rr:
                                    json.dump(order_log,rr,indent=4)



                            









                    







                    



                            


                                                


















        

            




        

                





    




        



        




        




        















                    







        














            


        












            







            







            



      










                    



                

                









        

 
         
        








            





        


            






    









        
        #print(k)



        # for y,z ,n  in zip(revised_vwap_list,surya,k):
            
        #     x=y-(y/14)+z
        #     n['VWAP']=x
        







        # with open(r"C:\Users\dasho\vwap_demo_revised_testing.json",'w') as se:

           



        #     json.dump(main_data,se,indent=4)


        




                
                
            











            




        


        


        




















        
        









        

     
        







        



        


        






        
       





                    
                
        




        
        


        


       






