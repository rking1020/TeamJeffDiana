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


#print social

#social_frame = pd.DataFrame(data=social)


#print grouped['SENTIMENT']
#n = grouped['SENTIMENT'].value_counts()

#n.plot(kind='barh', stacked=True)
#plt.show()

# #print social_frame
FB = social.loc[social['SOURCE_TYPE'] == 'FACEBOOK']
FOR = social.loc[social['SOURCE_TYPE'] == 'FORUMS']
TW = social.loc[social['SOURCE_TYPE'] == 'TWITTER']

print FB
print FOR


d = {'FACEBOOK': FB['SENTIMENT'], 'TWEETER': TW['SENTIMENT'], 'FORUMS' : FOR['SENTIMENT'] }
df = pd.DataFrame(data=d)
#g_FOR = social
#g_TWEETER =

print df
df.plot(kind='bar', stacked=True)
plt.show()
# pdf_FB = FB['SENTIMENT'].value_counts()

 #pdf_FOR = FOR['SENTIMENT'].value_counts()
#pdf_TW = TW['SENTIMENT'].value_count()

# pdf_TW.plot(kind='bar', stacked=True)

#x = social_frame.sort(columns='SOURCE_TYPE')#, axis=1, ascending=True, inplace=False, na_position='last')
#print x
#sentiment = social['SENTIMENT']

#sorted_sentiment = sentiment.value_counts()

#facebook = social['']
#forums_sent =
#twitter_Sent =


#print sorted_sentiment




# getting the columns

prod_category = product_master['PRODUCT_CATEGORY']
#brand_name = product_master['BRAND_NAME']
product_num = product_master['PRODUCT_NBR']
product_desc = product_master['PRODUCT_DESCRIPTION']
total_line_amount = order_master['TOTAL_LINE_AMT']

host1 = product_airtime['HOST1']
host2 = product_airtime['HOST2']

#top3_prod = prod_category.value_counts()[:3]

## look into moving the key
#pd.DataFrame(prod_category.value_counts()[:3]).plot(kind='pie', subplots=True, figsize=(8, 4))

#df.plot(kind='pie', subplots=True, figsize=(8, 4))

## Plot the bar graph
#plt.plot(range(1,11,1),top10_prod)
#plt.show()

#print product_airtime.sort(['HOST1'])










