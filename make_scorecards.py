#IMPORT
import pandas as pd
import sys
import numpy as np
from bs4 import BeautifulSoup, Tag
import re
from ast import literal_eval


def populate_scorecard(data):
	
    for index, row in data.iterrows():
        print('Making Scorecard for BERDO ID',int(row['BERDO_ID']))

        euis=row['EUIs'][1:-1].split()
        euis=[float(i) for i in euis]
        #print(euis)

        pctred=row['Percent_Reduction_EUI']
        
        if row['Most_Recent_ENERGY_STAR_Score'] == 'Not Available':
            print('Energy Star Score', 'Not Available for BERDO ID',int(row['BERDO_ID']))
        else:
            if pctred<0:
                pctred=abs(pctred)
                #OPEN SCORECARD HTML TEMPLATE
                with open("templates/scorecard_TEMPLATE_v2.html") as fp:
                    soup = BeautifulSoup(fp,features="html.parser")

            else:
                #OPEN SCORECARD HTML TEMPLATE
                with open("templates/scorecard_TEMPLATE_v1.html") as fp:
                    soup = BeautifulSoup(fp)
                #soup

            #POPULATE SCORECARD 
            finditem=["TEMPLATE_NAME","TEMPLATE_ADDRESS","TEMPLATE_BID",'TEMPLATE_GFA','TEMPLATE_PROPERTY_TYPE',
                      'TEMPLATE_YEAR_ESS','TEMPLATE_ESS','TEMPLATE_AVG_ESS',
                      'TEMPLATE_EUI_14', 'TEMPLATE_EUI_15', 'TEMPLATE_EUI_16', 'TEMPLATE_EUI_17', 'TEMPLATE_EUI_18', 
                      'TEMPLATE_EUI_PT_AVG','TEMPLATE_PCT_REDUCTION','TEMPLATE_EUI_BASE_YEAR','TEMPLATE_ESTIMATED_SAVINGS']
           #WITH ROWS FROM THE DATA SET
            replitem=[row['Property_Name'], row['Address'], str(int(row['BERDO_ID'])),str(format(round(row['GFA']), ",d")),row['Primary_Property_Type'],
                      str(row['Energy_Star_Score_Year']),str(row['Most_Recent_ENERGY_STAR_Score']),str(row['Average_Energy_Star_Score']),
                      str(euis[0]),str(euis[1]),str(euis[2]),str(euis[3]),str(euis[4]),
                      str(row['Property_Type_Average']),str(pctred),str(euis[0]),str(format(round(row['Possible_Savings']), ",d"))]

            for i in range(0,len(finditem)):
                finditm = soup.find_all(text = re.compile(finditem[i]))
                for comment in finditm:
                    fixed_text = comment.replace(finditem[i], replitem[i])
                    comment.replace_with(fixed_text)

            html = soup.prettify("utf-8")
            fn="scorecards/BERDO_scorecard_"+str(int(row['BERDO_ID']))+".html"
            with open(fn, "wb") as file:
                file.write(html)
        
    return



## Load data - 
df=pd.read_csv('data/BERDO_scorecard_data_file_011620.csv')
populate_scorecard(df)
