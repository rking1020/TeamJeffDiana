__author__ = 'audihurrr'

import pandas as pd
import matplotlib.pyplot as plt

# separating the csv files
product_master = pd.read_csv('full_data/product_master.csv')
customer_master = pd.read_csv('full_data/customer_master.csv')
email_campaign = pd.read_csv('full_data/email_campaign.csv')
social = pd.read_csv('full_data/social.csv')
order_master = pd.read_csv('full_data/order_master.csv')
product_airtime = pd.read_csv('full_data/product_airtime.csv')


# #print social_frame
FB = social.loc[social['SOURCE_TYPE'] == 'FACEBOOK']
FOR = social.loc[social['SOURCE_TYPE'] == 'FORUMS']
TW = social.loc[social['SOURCE_TYPE'] == 'TWITTER']

print FB
print FOR


d = {'FACEBOOK': FB['SENTIMENT'], 'TWEETER': TW['SENTIMENT'], 'FORUMS' : FOR['SENTIMENT'] }
df = pd.DataFrame(data=d)

print df
df.plot(kind='bar', stacked=True)
plt.show()


prod_category = product_master['PRODUCT_CATEGORY']
brand_name = product_master['BRAND_NAME']
product_num = product_master['PRODUCT_NBR']
product_desc = product_master['PRODUCT_DESCRIPTION']
total_line_amount = order_master['TOTAL_LINE_AMT']

host1 = product_airtime['HOST1']
host2 = product_airtime['HOST2']

top3_prod = prod_category.value_counts()[:3]

## look into moving the key
#pd.DataFrame(prod_category.value_counts()[:3]).plot(kind='pie', subplots=True, figsize=(8, 4))

#df.plot(kind='pie', subplots=True, figsize=(8, 4))

## Plot the bar graph
#plt.plot(range(1,11,1),top10_prod)
#plt.show()

#print product_airtime.sort(['HOST1'])
