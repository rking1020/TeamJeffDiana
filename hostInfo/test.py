'''
Created on Oct 17, 2015

@author: emiliedoyle
'''
# Import all of the necessary libraries, significant ones being pandas, matplotlib, numpy, csv. Pandas is important because it 
# is great at handling big data sets and also CSV files, which is how the data was presented to us. Numpy is great for calculations
# and matplotlib is excellent for plotting. 
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from collections import Counter
import csv
from matplotlib.tests.test_simplification import nan
from _ast import operator
from csamtools import itertools
from numpy import double
from StdSuites.Type_Names_Suite import rotation

# The CSV file 'product_airtime' is read in and parsed by the different columns. The column data is then turned to something 
# usable through ix. Each column gets its own structure
df=pd.read_csv('product_airtime.csv', names=['PRODUCT_NBR','ONAIR_DATE','ONAIR_START_TMS','ONAIR_END_TMS','ONAIR_MINS','HOST1','HOST2'])
#print df.ix[:,'PRODUCT_NBR']
#print df

#plt.plot(df.ix[:,'PRODUCT_NBR'], df.ix[:,'ONAIR_MINS'])
#plt.pie(df.ix[:,float('ONAIR_MINS')]);
#df.plot(x='PRODUCT_NBR', y='ONAIR_MINS')

product_nbr= df.ix[:,'PRODUCT_NBR']
onair_date=df.ix[:,'ONAIR_DATE']
onair_start_tms= df.ix[:,'ONAIR_START_TMS']
onair_end_tms=df.ix[:,'ONAIR_END_TMS']
onair_mins=df.ix[:,'ONAIR_MINS']
host1= df.ix[:,'HOST1']
host2=df.ix[:,'HOST2']

#get unique set of hosts
k=0
k2=0
host1_u= set()
for x in host1:
    if(x != 'HOST1'):    
        host1_u.add(x)
        k=k+1
host1_u=list(host1_u)
#print host1_u
host2_u=set()
for x in host2:
    if(x != 'HOST2'):
        host2_u.add(x)
        k2=k2+1
#print host2_u


#Get number of times that each host is listed
h1numbers= Counter(host1)
#print h1numbers
h2numbers=Counter(host2)
#print h2numbers
#plot for host 1 option
labels1, values= zip(*Counter(host1).items())
indexes=np.arange(len(labels1))
width=1
plt.bar(indexes, values, width)
plt.xticks(indexes+width*0.5, labels1, rotation=30)
plt.title('Instances Attributed to Host 1')
#plt.show(1)    
#plot for host 2 option
labels2, values= zip(*Counter(host2).items())
indexes=np.arange(len(labels2))
width=1
plt.bar(indexes, values, width)
plt.xticks(indexes+width*0.5, labels2)
plt.title('Instances Attributed to Host 2')
#plt.show(2)   


# Finding the onair minutes of the unique hosts
h1_ut=[0 for i in range(27)]
h2_ut=[0 for i in range(27)]
for x in range(len(onair_mins)):
        for a in range(27):
            if(host1[x]==host1_u[a]):
                h1_ut[a]= h1_ut[a]+ float(onair_mins[x])
            #if(host2[x]==host2_u[a]):
              #  h2_ut[a]= h2_ut[a]+float(onair_mins[x])
#print h1_ut
i=0
ind=[i for i in range(len(h1_ut))]
#print ind
#print labels1
plt.bar(ind, h1_ut, width)
#plt.show(3)

# Find the top 10 Primary and Secondary Hosts
# Indexing here starts at 1 because the "most time broadcasting" host is actually no host at all (ie online presence) 
h1_top10_time= h1_ut[1:11]
print 'h1 top 10 times', h1_top10_time
h1_top10_hosts= labels1[1:11]
print 'h1 top 10 hosts', h1_top10_hosts

h2_top10_time= h2_ut[1:11]
#print 'h2 top 10 times' ,h2_top10_time
h2_top10_hosts= labels2[1:11]
#print 'h2 top 10 hosts' ,h2_top10_hosts

# Create a bar graph of the top 10 hosts and their airtime
ind1=np.arange(10)
plt.bar(ind1, h1_top10_time, width)
plt.xticks(ind1+width*0.25, h1_top10_hosts, rotation=45)
plt.title('Top Ten Hosts 1 Cumulative On-Air Minutes')
#plt.show(4)

# Vaughn provided the product ids of the best selling items to look for trends with hosts, stored in top10prodId. Given these IDs
# I looped through the product numbers and if they matched the ones Vaughn provided, then I determined the host associated with that
# product and store them in another strucutre (top10prodHost1 or top10prodHost2)
top10prodHost1=[0 for i in range(10)]
top10prodHost2=[0 for i in range(10)]
top10prodId=['P150062267', 'P150015938', 'P150028599', 'P150017959', 'P150067321', 'P150033578', 'P150018383', 'P150065551', 'P150015937', 'P150016602']
for x in range(len(product_nbr)):
    for a in range(10):
        if(product_nbr[x]==top10prodId[a]):
            top10prodHost1[a]=host1[x]
            top10prodHost2[a]=host2[x]
print 'top 10 products host1' ,top10prodHost1
print 'top 10 products host2' ,top10prodHost2

