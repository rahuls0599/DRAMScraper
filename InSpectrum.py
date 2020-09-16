#INSYE.COM
import pandas as pd
from lxml import html
import requests
from datetime import datetime
import sys
from os import path


#Exit from program if values are updated for today
if(path.exists('InsyeContractPrice.csv')):
    df = pd.read_csv('InsyeContractPrice.csv', 'r')
    x = datetime.now()
    if((df.iloc[-1, 0])[:2] == x.strftime("%d")):
        sys.exit("All programs have already been run today and values have been updated")

#List of webpages to access
webpages = ['http://www.insye.com/dram/', 'http://www.insye.com/nand/']
updation_date=""
appending_spot_price = {}
appending_spot_price_change = {}
appending_contract_price = {}
appending_contract_price_change = {}

#Further working on each webpage
for webpage in webpages:
    #For determining if we are scraping currently spot table or contract table
    for i in range(2):   
        #Accessing each webpage
        page = requests.get(webpage)
        tree = html.fromstring(page.content)
                
        #Scraping the values and appending them
        if(webpage == webpages[0]):
            if(i==0):
                print("\nDRAM Spot")
                #Appending date to new row
                #updation_date = tree.xpath('//*[@id="table_30_row_0"]/td[6]')[0].text[:10]
                updation_date = datetime.now().date().strftime("%d %B %Y")
                appending_spot_price['Date'] = str(updation_date).replace('/','-')
                appending_contract_price['Date'] = str(updation_date).replace('/','-')
                appending_contract_price_change['Date'] = str(updation_date).replace('/','-')
                appending_spot_price_change['Date'] = str(updation_date).replace('/','-')
                
                for j in range(12):
                    text = tree.xpath('//*[@id="table_30_row_' + str(j) + '"]/td[1]')[0].text
                    average_value = tree.xpath('//*[@id="table_30_row_' + str(j) + '"]/td[4]')[0].text
                    appending_spot_price[text.strip()] = str(average_value)
                    average_value_change = tree.xpath('//*[@id="table_30_row_' + str(j) + '"]/td[5]')[0].text
                    appending_spot_price_change[text.strip()] = str(average_value_change)
                    print(text.strip(),"--", average_value,"--",average_value_change)
                
            else:
                print("\nDRAM Contract\n")
                
                for j in range(6):
                    text = tree.xpath('//*[@id="table_19_row_' + str(j) + '"]/td[1]')[0].text
                    average_value = tree.xpath('//*[@id="table_19_row_' + str(j) +'"]/td[4]')[0].text
                    appending_contract_price[text.strip()] = str(average_value)
                    average_value_change = tree.xpath('//*[@id="table_19_row_' + str(j) + '"]/td[5]')[0].text
                    appending_contract_price_change[text.strip()] = str(average_value_change)
                    print(text.strip(),"--", average_value,"--",average_value_change)
                    
        else:
            if(i==0):
                print("\nNAND Spot\n")
                #Appending date to new row
                
                for j in range(3):
                    text = tree.xpath('//*[@id="table_26_row_' + str(j) + '"]/td[1]')[0].text
                    average_value = tree.xpath('//*[@id="table_26_row_' + str(j) +'"]/td[4]')[0].text
                    appending_spot_price[text.strip()] = str(average_value)
                    average_value_change = tree.xpath('//*[@id="table_26_row_' + str(j)+ '"]/td[5]')[0].text
                    appending_spot_price_change[text.strip()] = str(average_value_change)
                    print(text.strip(),"--", average_value,"--",average_value_change)
                
            else:
                print("\nNAND Contract\n")
                
                for j in range(4):
                    text = tree.xpath('//*[@id="table_20_row_' + str(j) + '"]/td[1]')[0].text
                    average_value = tree.xpath('//*[@id="table_20_row_' + str(j) +'"]/td[4]')[0].text
                    appending_contract_price[text.strip()] = str(average_value)
                    average_value_change = tree.xpath('//*[@id="table_20_row_' + str(j) + '"]/td[7]')[0].text
                    appending_contract_price_change[text.strip()] = str(average_value_change)
                    print(text.strip(),"--", average_value,"--",average_value_change)
                

df_spot_price = pd.read_csv("InsyeSpotPrice.csv")
#df_spot_change = pd.read_csv("InsyeSpotPriceChange.csv")
df_contract_price = pd.read_csv("InsyeContractPrice.csv")
df_contract_change = pd.read_csv("InsyeContractPriceChange.csv")

df_contract_price = df_contract_price.append(appending_contract_price, ignore_index=True)
df_contract_change = df_contract_change.append(appending_contract_price_change, ignore_index=True)
df_spot_price = df_spot_price.append(appending_spot_price, ignore_index=True)
#df_spot_change = df_spot_change.append(appending_spot_price_change, ignore_index=True)

df_spot_price.to_csv("InsyeSpotPrice.csv", index=False)
#df_spot_change.to_csv("InsyeSpotPriceChange.csv", index=False)
df_contract_price.to_csv("InsyeContractPrice.csv", index=False)
df_contract_change.to_csv("InsyeContractPriceChange.csv", index=False)