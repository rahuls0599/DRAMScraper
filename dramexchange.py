#DRAMEXCHANGE.COM
from lxml import html
import requests
from datetime import datetime
import sys
from os import path
import pandas as pd

if(path.exists('DxSpotPrice.csv')):
    #Exit from program if values are updated for today
    df = pd.read_csv('DxSpotPrice.csv', 'r')
    x = datetime.now()
    if((df.iloc[-1, 0])[:2] == str(x.strftime("%d"))):
        sys.exit("All programs have already been run today and values have been updated")

def get_gbs(link_text):
    gbs = ""
    name_of_item = link_text.text_content().strip()
    last_index = name_of_item.find("G") - 1
    for i in range(3):
        if(name_of_item[last_index - i] == ' '):
            break
        else:
            gbs = name_of_item[last_index - i]+gbs
    return gbs

#Accessing the webpage
page = requests.get("http://www.dramexchange.com").text
doc = html.fromstring(page)

#tbody id values
tbody_ids_1 = ['NationalDramSpotPrice', 'NationalFlashSpotPrice', 'MemCardSpotPrice', 'eMMCSpotPrice']
#tbody_ids_2 = ['PCC_Price', 'NationalDramContractPrice', 'NationalFlashContractPrice'] 

df = pd.read_csv("DxSpotPrice.csv")
appending_price = {}
appending_normalised = {}
appending_pergb = {}

#Implementing the scraping procedure for Spot Prices
for tbody_id in tbody_ids_1:
    
    #For Spot or Contract values
    if (tbody_id == tbody_ids_1[0]):
        print("\nDRAM Spot\n")
        #Updation Date
        link_text_date = doc.cssselect("#NationalDramSpotPrice_show_day > span")[0]
        #updation_date = date_formatting(link_text_date)
        updation_date = datetime.now().date().strftime("%d %B %Y")
        
        #Appending date to file
        appending_price['Date'] = updation_date
        appending_normalised['Date'] = updation_date
        appending_pergb['Date'] = updation_date
        
        appending_price['Category'] = "Spot Prices"
        appending_normalised['Category'] = "Normalized Spot Prices"
        appending_pergb['Category'] = "Spot - $ Per GB"

        #Scrape the values and append them to file
        for i in range(6):
            
            #Item Name
            link_text = doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td.tab_tr_gray2 > a")[0]
            #appending_spot_name.append(link_text.text_content().strip())
            
            #Session Average
            link_value = doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td:nth-child(6)")[0]
            average_value = float(link_value.text_content().strip())
            appending_price[link_text.text_content().strip()] = str(average_value)
            
            #Normalised Value
            #high_value = float(doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td:nth-child(4)")[0].text_content().strip())
            #low_value = float(doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td:nth-child(5)")[0].text_content().strip())
            normalised_value = average_value / df[link_text.text_content().strip()].loc[df[link_text.text_content().strip()].first_valid_index()]
            appending_normalised[link_text.text_content().strip()] = str(normalised_value)
            
            #Price per GB
            gbs = get_gbs(link_text)
            value_per_gb = average_value/float(gbs)
            appending_pergb[link_text.text_content().strip()] = str(value_per_gb)
            
            print(link_text.text_content().strip(),"--", average_value,"--",value_per_gb,"--",normalised_value)
            
            
    elif (tbody_id == tbody_ids_1[1]):
        print("\nFlash Spot\n")
        
        #Scrape the values and append them to file
        for i in range(5):
            
            #Item Name
            link_text = doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td.tab_tr_gray2 > a")[0]
            #appending_spot_name.append(link_text.text_content().strip())
            
            #Session Average
            link_value = doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td:nth-child(6)")[0]
            average_value = float(link_value.text_content().strip())
            appending_price[link_text.text_content().strip()] = str(average_value)
            
            #Normalised value
            #high_value = float(doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td:nth-child(4)")[0].text_content().strip())
            #low_value = float(doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td:nth-child(5)")[0].text_content().strip())
            normalised_value = average_value / df[link_text.text_content().strip()].loc[df[link_text.text_content().strip()].first_valid_index()]
            appending_normalised[link_text.text_content().strip()] = str(normalised_value)
            
            #Price per GB
            gbs = get_gbs(link_text)
            value_per_gb = average_value/float(gbs)
            appending_pergb[link_text.text_content().strip()] = str(value_per_gb)
            
            print(link_text.text_content().strip(),"--", average_value,"--",value_per_gb,"--",normalised_value)
            
            
    elif (tbody_id == tbody_ids_1[2]):
        print("\nMem Spot\n")
        
        #Scrape the values and append them to file
        for i in range(4):
            
            #Item Name
            link_text = doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td.tab_tr_gray2 > a")[0]
            #appending_spot_name.append(link_text.text_content().strip())
            
            #Session Average
            link_value = doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td:nth-child(6)")[0]
            average_value = float(link_value.text_content().strip())
            appending_price[link_text.text_content().strip()] = str(average_value)
            
            #Normalised Value
            #high_value = float(doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td:nth-child(4)")[0].text_content().strip())
            #low_value = float(doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td:nth-child(5)")[0].text_content().strip())
            normalised_value = average_value / df[link_text.text_content().strip()].loc[df[link_text.text_content().strip()].first_valid_index()]
            appending_normalised[link_text.text_content().strip()] = str(normalised_value)
            
            #Price per GB
            gbs = get_gbs(link_text)
            value_per_gb = average_value/float(gbs)
            appending_pergb[link_text.text_content().strip()] = str(value_per_gb)
            
            print(link_text.text_content().strip(),"--", average_value,"--", value_per_gb,"--",normalised_value)
            
    else:
        print("\neMMC Spot\n")
        
        #Scrape the values and append them to file
        for i in range(3):
            
            #Item Name
            link_text = doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td.tab_tr_gray2 > a")[0]
            #appending_spot_name.append(link_text.text_content().strip())
            
            #Session Average
            link_value = doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td:nth-child(6)")[0]
            average_value = float(link_value.text_content().strip())
            appending_price[link_text.text_content().strip()] = str(average_value)
            
            #Normalised Value
            #high_value = float(doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td:nth-child(4)")[0].text_content().strip())
            #low_value = float(doc.cssselect("#tb_" + tbody_id + " > tr:nth-child(" + str(i+2) + ") > td:nth-child(5)")[0].text_content().strip())
            normalised_value = average_value / df[link_text.text_content().strip()].loc[df[link_text.text_content().strip()].first_valid_index()]
            appending_normalised[link_text.text_content().strip()] = str(normalised_value)
            
            
            #Price per GB
            gbs = get_gbs(link_text)
            value_per_gb = average_value/float(gbs)
            appending_pergb[link_text.text_content().strip()] = str(value_per_gb)
            
            print(link_text.text_content().strip(),"--", average_value,"--", value_per_gb,"--",normalised_value)

df_price = pd.read_csv('DxSpotPrice.csv')
df_normalised = pd.read_csv('DxSpotPriceNormalised.csv')
df_pergb = pd.read_csv('DxSpotPricePerGb.csv')

df_price = df_price.append(appending_price, ignore_index=True)
df_normalised = df_normalised.append(appending_normalised, ignore_index=True)
df_pergb = df_pergb.append(appending_pergb, ignore_index=True)

df_price.to_csv('DxSpotPrice.csv', index=False)
df_normalised.to_csv('DxSpotPriceNormalised.csv', index=False)
df_pergb.to_csv('DxSpotPricePerGb.csv', index=False)