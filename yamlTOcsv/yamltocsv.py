#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import yaml

fieldnames = ['DATE','NUMBER', 'FF','CLASS','FARE','FROM', 'STATUS', 'TO']

with open('Egor_loh.csv', 'w', newline='') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames=fieldnames)
    csv_output.writeheader()

    for filename in ['SkyTeam-Exchange.yaml']:
        with open(filename) as f_input:
            data = yaml.safe_load(f_input)
            for item,doc in data.items():
                row3={'DATE' : item}
                row1={'DATE' : item}
                row={'DATE' : item}
                for item2, doc2 in doc.items():
                    row2= {'NUMBER' : item2}
                    for item3,doc3 in doc2.items():
                        for get in ['FROM', 'STATUS', 'TO']:
                            row3[get] = doc2[get]
                        if item3=='FF':
                                for item4,doc4 in doc3.items():
                                    row4={'FF' : item4}
                                    for item5,doc5 in doc4.items():
                                        for gett in ['CLASS','FARE']:
                                            row = row3
                                            row['FF'] = row4['FF']
                                            row['NUMBER'] = row2['NUMBER']
                                            row['DATE'] = row1['DATE']
                                            row[gett] = doc4[gett]
                                    csv_output.writerow(row)


# In[ ]:





# In[ ]:




