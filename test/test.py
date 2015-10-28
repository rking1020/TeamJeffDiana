'''
Created on Oct 17, 2015

@author: emiliedoyle
'''
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from collections import Counter
from matplotlib.tests.test_simplification import nan
from _ast import operator
from csamtools import itertools
from numpy import double
from StdSuites.Type_Names_Suite import rotation
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
plt.show(1)    
#plot for host 2 option
labels2, values= zip(*Counter(host2).items())
indexes=np.arange(len(labels2))
width=1
plt.bar(indexes, values, width)
plt.xticks(indexes+width*0.5, labels2)
plt.title('Instances Attributed to Host 2')
plt.show(2)   
#Finding unique hosts
h1_ut=[0 for i in range(27)]
for x in range(len(onair_mins)):
        for a in range(27):
            if(host1[x]==host1_u[a]):
                h1_ut[a]= h1_ut[a]+ float(onair_mins[x])
#print h1_ut
i=0
ind=[i for i in range(len(h1_ut))]
#print ind
#print labels1
plt.bar(ind, h1_ut, width)
plt.show(3)

h1_top5_time= h1_ut[1:6]
#print h1_top5_time
h1_top5_hosts= labels1[1:6]
#print h1_top5_hosts
ind1=np.arange(5)
plt.bar(ind1, h1_top5_time, width)
plt.xticks(ind1+width*0.25, h1_top5_hosts, rotation=45)
plt.title('Top Five Hosts 1 Cumulative On-Air Minutes')
plt.show(4)

# Get vaughn to give the product ids of the best selling items to look for trends with hosts

