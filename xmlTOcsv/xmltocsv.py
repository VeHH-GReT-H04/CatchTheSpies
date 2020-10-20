#!/usr/bin/env python
# coding: utf-8

# In[90]:


import xml.etree.ElementTree as ET
import csv

my_file = 'PointzAggregator-AirlinesData.xml'

fieldnames = ['LAST','FIRST','NONAME','FROM','TO','FROMDATE','FROMTIME','TODATE','TOTIME']
with open('loh2.csv', 'w', newline='') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames=fieldnames)
    csv_output.writeheader()

    tree = ET.parse(my_file)
    root = tree.getroot()

    for time in root.findall('user'):
        last = time.find('name').get('last')
        first = time.find('name').get('first')
        for time1 in time.findall('cards'):
            for time2 in time1.findall('card'):
                for time3 in time2.findall('activities'):
                    for time4 in time3.findall('activity'):
                        Date = time4.find('Date').text
                        Departure = time4.find('Departure').text
                        Arrival = time4.find('Arrival').text
                        row={'LAST': last,'FIRST': first,'FROM': Departure,'TO': Arrival,'FROMDATE': Date}
                        csv_output.writerow(row)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




