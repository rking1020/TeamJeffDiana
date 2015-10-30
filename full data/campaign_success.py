#!/usr/bin/env python


import csv
import sys

def main(argv):

    
    fieldnames = ['MONTH', 'CATEGORY', 'SPEND_SUM']

    al=[0.0,0.0,0.0]    # All
    acc=[0.0,0.0,0.0]    # Accessories
    app=[0.0,0.0,0.0]    # Apparel
    aa=[0.0,0.0,0.0]    # Apparel & Accessories
    aaj=[0.0,0.0,0.0]    # Apparel, Accessories & Jewelry
    aajb=[0.0,0.0,0.0]    # Apparel, Accessories, Jewelry & Beauty
    bea=[0.0,0.0,0.0]    # Beauty
    elec=[0.0,0.0,0.0]    # Electronics
    hg=[0.0,0.0,0.0]    # Home & Garden
    jw = [0.0,0.0,0.0]    # Jewelry
    kf=[0.0,0.0,0.0]    # Kitchen & Food
    
    # Read the data from the csv
    try:
        with open('email_campaign.csv', 'rb') as emailfile:
            emailreader = csv.DictReader(emailfile, quotechar='"', delimiter=',')
            # Write the modified 
            with open('result.csv', 'wb') as resultfile:
                rwriter = csv.DictWriter(resultfile, fieldnames=fieldnames) 
                rwriter.writeheader()
                rwriter.writerow({'MONTH':'Dec', 'CATEGORY':'Fun', 'SPEND_SUM':50})
                
                for row in emailreader:
                                        
                    print((row['PRODUCT_CATEGORY']))
                    if(row['CAMPAIGN_DATE'].startswith("1/")):
                        #month="January"
                        if(row['PRODUCT_CATEGORY']=='All'):
                            al[0]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Accessories'):
                            acc[0]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Apparel'):
                            app[0]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Apparel & Accessories'):
                            aa[0]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Apparel, Accessories & Jewelry'):
                            aaj[0]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Apparel, Accessories, Jewelry & Beauty'):
                            aajb[0]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Beauty'):
                            bea[0]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Electronics'):
                            elec[0]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Home & Garden'):
                            hg[0]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Jewelry'):
                            jw[0]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Kitchen & Food'):
                            kf[0]+=float(row['CAMPAIGN_SPEND'])
                        else:
                            print("OH MAN. WE LOST SOMETHING IN JAN")

                    elif(row['CAMPAIGN_DATE'].startswith("2/")):
                        #
                        #month="February"
                        if(row['PRODUCT_CATEGORY']=='All'):
                            al[1]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Accessories'):
                            acc[1]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Apparel'):
                            app[1]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Apparel & Accessories'):
                            aa[1]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Apparel, Accessories & Jewelry'):
                            aaj[1]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Apparel, Accessories, Jewelry & Beauty'):
                            aajb[1]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Beauty'):
                            bea[1]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Electronics'):
                            elec[1]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Home & Garden'):
                            hg[1]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Jewelry'):
                            jw[1]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Kitchen & Food'):
                            kf[1]+=float(row['CAMPAIGN_SPEND'])
                        else:
                            print("OH MAN. WE LOST SOMETHING IN FEB")
                    elif(row['CAMPAIGN_DATE'].startswith("3/")):
                        #month="MARCH"
                        if(row['PRODUCT_CATEGORY']=='All'):
                            al[2]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Accessories'):
                            acc[2]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Apparel'):
                            app[2]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Apparel & Accessories'):
                            aa[2]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Apparel, Accessories & Jewelry'):
                            aaj[2]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Apparel, Accessories, Jewelry & Beauty'):
                            aajb[2]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Beauty'):
                            bea[2]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Electronics'):
                            elec[2]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Home & Garden'):
                            hg[2]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Jewelry'):
                            jw[2]+=float(row['CAMPAIGN_SPEND'])
                        elif(row['PRODUCT_CATEGORY']=='Kitchen & Food'):
                            kf[2]+=float(row['CAMPAIGN_SPEND'])
                        else:
                            print("OH MAN. WE LOST SOMETHING IN MARCH")
                    else:
                        print("Unidentified month")


                rwriter.writerow({'MONTH':'January', 'CATEGORY':'All', 'SPEND_SUM':al[0]})
                rwriter.writerow({'MONTH':'January', 'CATEGORY':'Accessories', 'SPEND_SUM':acc[0]})
                rwriter.writerow({'MONTH':'January', 'CATEGORY':'Accessories & Apparel', 'SPEND_SUM':aa[0]})
                rwriter.writerow({'MONTH':'January', 'CATEGORY':'Accessories, Apparel & Jewelry', 'SPEND_SUM':aaj[0]})
                rwriter.writerow({'MONTH':'January', 'CATEGORY':'Accessories, Apparel, Jewelry & Beauty', 'SPEND_SUM':aajb[0]})
                rwriter.writerow({'MONTH':'January', 'CATEGORY':'Beauty', 'SPEND_SUM':bea[0]})
                rwriter.writerow({'MONTH':'January', 'CATEGORY':'Electronics', 'SPEND_SUM':elec[0]})
                rwriter.writerow({'MONTH':'January', 'CATEGORY':'Home & Garden', 'SPEND_SUM':hg[0]})
                rwriter.writerow({'MONTH':'January', 'CATEGORY':'Jewelry', 'SPEND_SUM':jw[0]})
                rwriter.writerow({'MONTH':'January', 'CATEGORY':'Kitchen & Flood', 'SPEND_SUM':kf[0]})


                rwriter.writerow({'MONTH':'February', 'CATEGORY':'All', 'SPEND_SUM':al[1]})
                rwriter.writerow({'MONTH':'February', 'CATEGORY':'Accessories', 'SPEND_SUM':acc[1]})
                rwriter.writerow({'MONTH':'February', 'CATEGORY':'Accessories & Apparel', 'SPEND_SUM':aa[1]})
                rwriter.writerow({'MONTH':'February', 'CATEGORY':'Accessories, Apparel & Jewelry', 'SPEND_SUM':aaj[1]})
                rwriter.writerow({'MONTH':'February', 'CATEGORY':'Accessories, Apparel, Jewelry & Beauty', 'SPEND_SUM':aajb[1]})
                rwriter.writerow({'MONTH':'February', 'CATEGORY':'Beauty', 'SPEND_SUM':bea[1]})
                rwriter.writerow({'MONTH':'February', 'CATEGORY':'Electronics', 'SPEND_SUM':elec[1]})
                rwriter.writerow({'MONTH':'February', 'CATEGORY':'Home & Garden', 'SPEND_SUM':hg[1]})
                rwriter.writerow({'MONTH':'February', 'CATEGORY':'Jewelry', 'SPEND_SUM':jw[1]})
                rwriter.writerow({'MONTH':'February', 'CATEGORY':'Kitchen & Flood', 'SPEND_SUM':kf[1]})


                rwriter.writerow({'MONTH':'March', 'CATEGORY':'All', 'SPEND_SUM':al[2]})
                rwriter.writerow({'MONTH':'March', 'CATEGORY':'Accessories', 'SPEND_SUM':acc[2]})
                rwriter.writerow({'MONTH':'March', 'CATEGORY':'Accessories & Apparel', 'SPEND_SUM':aa[2]})
                rwriter.writerow({'MONTH':'March', 'CATEGORY':'Accessories, Apparel & Jewelry', 'SPEND_SUM':aaj[2]})
                rwriter.writerow({'MONTH':'March', 'CATEGORY':'Accessories, Apparel, Jewelry & Beauty', 'SPEND_SUM':aajb[2]})
                rwriter.writerow({'MONTH':'March', 'CATEGORY':'Beauty', 'SPEND_SUM':bea[2]})
                rwriter.writerow({'MONTH':'March', 'CATEGORY':'Electronics', 'SPEND_SUM':elec[2]})
                rwriter.writerow({'MONTH':'March', 'CATEGORY':'Home & Garden', 'SPEND_SUM':hg[2]})
                rwriter.writerow({'MONTH':'March', 'CATEGORY':'Jewelry', 'SPEND_SUM':jw[2]})
                rwriter.writerow({'MONTH':'March', 'CATEGORY':'Kitchen & Flood', 'SPEND_SUM':kf[2]})
                
            
               # except IOError:
                #    print "I can't write stuff"

    except IOError:
        print "Error: File may not exist"
    

                
            
           # print(row['CAMPAIGN_DATE'], row['PRODUCT_CATEGORY'], row['CAMPAIGN_SPEND'])

#with open('order_master.csv', 'rb') as orderfile:
#    orderreader = csv.DictReader(orderfile, delimiter=',', quotechar='|')
#    for row in orderreader:
#        print(row['TOTAL_LINE_AMT'], row['ORDER_TIME'])
        
# begin gracefully
#
if __name__=="__main__":
    main(sys.argv[1:])
#
# end of file
     
