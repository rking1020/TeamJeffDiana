'''
Created on Oct 30, 2015
This is to make a CSV file of just the total line amount from the order master CSV, so it can be processed easily in c++ w/o concerns for typing
@author: emiliedoyle
'''
import pandas as pd
import csv
df=pd.read_csv('order_master.csv', names=['ORDER_NBR','ORDER_LINE_NBR','CUSTOMER_\
NBR','PRODUCT_NBR','ORDER_PLATFORM','ORDER_DATE','ORDER_TIME','TOTAL_LINE_AMT'])
total_line_amt= df.ix[:,'TOTAL_LINE_AMT']

with open('totLineAmt.csv', 'wb') as myfile:
    wr= csv.writer(myfile)
    wr.writerow(total_line_amt)
print 'done'