import csv
import numpy
from datetime import datetime, date, time

# Some constants used later for month iterations
_JAN_ = 1
_FEB_ = 2
_MAR_ = 3

# Category Constants
_APPAREL_ = "Apparel"
_ACCESSORIES_= "Accessories"
_HOME_DECOR_ = "Home Decor"
_GIFT_CARDS_ = "Gift Cards"
_HEALTH_BEAUTY_ = "Health/Beauty"
_TEXTILE_FURNIT_ = "Textile/Furnit"
_IQVC_DIVSIONAL_ = "IQVC Divisional"
_ENTERTAINMENT_ = "Entertainment"
_COLLECTIBLES_ = "Collectibles"
_ELECTRONICS_ = "Electronics"
_JEWELRY_ = "Jewelry"
_RETURNS_ = "Returns"
_PUBLIC_RELATION_ = "PUBLIC RELATION"
_COSTUME_JEWELRY_ = "Costume Jewelry"
_HOUSEWARES_ = "Housewares"
_HEALTH_ = "Health"
_LICENSE_HARDGOODS_ = "License Hardgds"
_FUN_LEISURE_ = "Fun & Leisure"
_APP_ACCESS_EVENT_ = "App/Accss Event"

_PRODUCT_MASTER_ = "product_master.csv"
_ORDER_MASTER_ = "order_master.csv"

apparel_sum = 0
accessories_sum= 0
home_decor_sum = 0
gift_card_sum = 0
health_beauty_sum = 0
textile_furnit_sum = 0
iqvc_div_sum = 0
entertainment_sum = 0
collectibles_sum = 0
electronics_sum = 0
jewelry_sum = 0
returns_sum = 0
public_relations_sum = 0
costume_jewelry_sum = 0
housewares_sum = 0
health_sum = 0
license_hardgoods_sum = 0
fun_leisure_sum = 0
app_access_sum = 0

# Import the CSV Files
reader=csv.reader(open(_PRODUCT_MASTER_,"rb"),delimiter=',')
x=list(reader)
product_master=numpy.array(x)

reader=csv.reader(open(_ORDER_MASTER_, "rb"), delimiter=',')
x=list(reader)
order_master=numpy.array(x)



#  ORDER_MASTER
#
#   1). Data should look as follows:
#       a).  ['PRODUCT_NBR', 'TOTAL_LINE_AMOUNT' , 'ORDER_DATE']
#
#
#   PRODUCT_MASTER
#
#   1). CSV File should look as follows;
#       a).  ['PRODUCT_NBR', 'PRODUCT_CATEGORY']
#


# Removes the COLUMN LABEL
product_master=product_master[1:,:]

order_master=order_master[1:,:]

# Sort the PRODUCT MASTER file
sorted_product_master = product_master[product_master[:,0].argsort()]

# recursive binary search function
def ndarrayBinSearch(array, target):

    """

    :rtype : basestring
    """
    n = array[:,1].size
    if (n==0):
        return 0
    else:
        midpoint = n/2
        if array[midpoint,0]==target:
            retval = array[midpoint,1]
            return retval
        else:
            if target < array[midpoint, 0]:
                return ndarrayBinSearch(array[:midpoint], target)
            else:
                return ndarrayBinSearch(array[midpoint:], target)




# Replace all the PRODUCT_NBRs in order_master with PRODUCT_CATEGORY in product_master
for i in range(0,49):
    for j in range((i*order_master[:,1].size), (order_master[:,1].size)/50*(i+1)):
        curProductNbr = order_master[j,0]
        assocProdCat = ndarrayBinSearch(sorted_product_master, curProductNbr)
        order_master[j,0] = assocProdCat

# ORDER_MASTER now contains PRODUCT_CATEGORY in place of PRODUCT_NBR

#Initialize the categories!

#Setting all sum variables to zero
#reset_sums()

#Iterate through every month (january, february, march)
# Calculate rolling sum for every PRODUCT_CATEGORY

for i in range(0, order_master[:,1].size):
    dt = datetime.strptime(str(order_master[i,2]), "%m/%d/%Y" )
    #
    if (dt.month==_FEB_):
        # calculate the corresponding PRODUCT_CATEGORY rolling sum for that month!
        if (order_master[i,0]==_APPAREL_):
            apparel_sum += float(order_master[i,1])
        if (order_master[i,0]==_ACCESSORIES_):
            accessories_sum += float(order_master[i,1])
        if (order_master[i,0]==_HOME_DECOR_):
            home_decor_sum += float(order_master[i,1])
        if (order_master[i,0]==_GIFT_CARDS_):
            gift_card_sum += float(order_master[i,1])
        if (order_master[i,0]==_HEALTH_BEAUTY_):
            health_beauty_sum += float(order_master[i,1])
        if (order_master[i,0]==_TEXTILE_FURNIT_):
            textile_furnit_sum += float(order_master[i,1])
        if (order_master[i,0]==_IQVC_DIVSIONAL_):
            iqvc_div_sum += float(order_master[i,1])
        if (order_master[i,0]==_ENTERTAINMENT_):
            entertainment_sum += float(order_master[i,1])
        if (order_master[i,0]==_COLLECTIBLES_):
            collectibles_sum += float(order_master[i,1])
        if (order_master[i,0]==_ELECTRONICS_):
            electronics_sum += float(order_master[i,1])
        if (order_master[i,0]==_JEWELRY_):
            jewelry_sum += float(order_master[i,1])
        if (order_master[i,0]==_RETURNS_):
            returns_sum += float(order_master[i,1])
        if (order_master[i,0]==_PUBLIC_RELATION_):
            public_relations_sum += float(order_master[i,1])
        if (order_master[i,0]==_COSTUME_JEWELRY_):
            costume_jewelry_sum += float(order_master[i,1])
        if (order_master[i,0]==_HOUSEWARES_):
            housewares_sum += float(order_master[i,1])
        if (order_master[i,0]==_HEALTH_):
            health_sum += float(order_master[i,1])
        if (order_master[i,0]==_LICENSE_HARDGOODS_):
            license_hardgoods_sum += float(order_master[i,1])
        if (order_master[i,0]==_FUN_LEISURE_):
            fun_leisure_sum += float(order_master[i,1])
        if (order_master[i,0]==_APP_ACCESS_EVENT_):
            app_access_sum += float(order_master[i,1])

print(_APPAREL_ + " sum : $" + str(apparel_sum))
print(_ACCESSORIES_ + " sum : $" + str(accessories_sum))
print(_HOME_DECOR_ + " sum : $" + str(home_decor_sum))
print(_GIFT_CARDS_ + " sum : $" + str(gift_card_sum))
print(_HEALTH_BEAUTY_ + " sum : $" + str(health_beauty_sum))
print(_TEXTILE_FURNIT_ + " sum : $" + str(textile_furnit_sum))
print(_IQVC_DIVSIONAL_ + " sum : $" + str(iqvc_div_sum))
print(_ENTERTAINMENT_ + " sum : $" + str(entertainment_sum))
print(_COLLECTIBLES_ + " sum : $" + str(collectibles_sum))
print(_ELECTRONICS_ + " sum : $" + str(electronics_sum))
print(_JEWELRY_ + " sum : $" + str(jewelry_sum))
print(_RETURNS_ + " sum : $" + str(returns_sum))
print(_PUBLIC_RELATION_ + " sum : $" + str(public_relations_sum))
print(_COSTUME_JEWELRY_ + " sum : $" + str(costume_jewelry_sum))
print(_HOUSEWARES_ + " sum : $" + str(housewares_sum))
print(_HEALTH_ + " sum : $" + str(health_sum))
print(_LICENSE_HARDGOODS_ + " sum : $" + str(license_hardgoods_sum))
print(_FUN_LEISURE_ + " sum : $" + str(fun_leisure_sum))
print(_APP_ACCESS_EVENT_ + " sum : $" + str(app_access_sum))

