#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os,datetime
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter, DayLocator
from matplotlib.ticker import FuncFormatter
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#sales_data = pd.read_csv('~/Downloads')
sales_data = pd.read_csv('C:/Users/SHIVARJUN/Downloads/SalesDataNoCancels.csv')


# In[3]:


sales_data.head()


# In[4]:


sales_data['InvoiceDate']=pd.to_datetime(sales_data['InvoiceDate'],
                    infer_datetime_format=True)
sales_data['Date']=sales_data['InvoiceDate'].dt.strftime('%m/%d/%Y')
sales_data['Date_Year'] = sales_data['InvoiceDate'].dt.strftime('%m/%Y')
sales_data['Time']=sales_data['InvoiceDate'].dt.strftime('%H:%M')
sales_data['Year']=sales_data['InvoiceDate'].dt.strftime('%Y')
sales_data['Month']=sales_data['InvoiceDate'].dt.strftime('%B')
sales_data['Day_of_Week']=sales_data['InvoiceDate'].dt.strftime('%A')
sales_data['Month']=sales_data['InvoiceDate'].dt.strftime('%B')
sales_data['Sales_Total']=sales_data['Quantity']*sales_data['UnitPrice']
sales_data.head()


# In[ ]:





# # Bar Chart of Number of Quantities sold in month/year

# In[5]:


salesby_qty_dateyear = sales_data.loc[:, ['Quantity', 'Date_Year']]
salesbygrp_qty_dateyear = salesby_qty_dateyear.groupby('Date_Year').sum() 
labels1=[x for x in salesbygrp_qty_dateyear.index]
plt.figure(figsize=(20,10))
plt.rc('xtick', labelsize=14) 
plt.rc('ytick', labelsize=14) 
plt.bar(labels1, salesbygrp_qty_dateyear['Quantity'], align='center', color=['black', 'red', 'green', 'blue', 'cyan'])
plt.xticks(labels1,rotation=65)
plt.ylabel('Number of Quantities',size=25)
plt.title('Number of Quantities sold by Month/Year ',size=25)


# In[ ]:





# # Bar Chart of Number of sales by county 

# In[6]:


sale_total_bycountry = sales_data.loc[:, ['Country', 'Sales_Total']]
grpby_sale_total_bycountry = sale_total_bycountry.groupby('Country').sum() 
labels3 =[x for x in grpby_sale_total_bycountry.index]
plt.figure(figsize=(20,10))
plt.ticklabel_format(style='plain')
plt.rc('xtick', labelsize=10) 
plt.rc('ytick', labelsize=10) 
plt.barh(labels3, grpby_sale_total_bycountry['Sales_Total'], color=['black', 'red', 'green', 'blue', 'cyan'])
plt.xlabel('sales total',size=10)
plt.title('Number of sales by country ',size=25)


# In[ ]:





# # Bar Chart of Total sales by Month/Year

# In[7]:


salestotal_dateyear = sales_data.loc[:, ['Sales_Total', 'Date_Year']]
salestotal_grp_dateyear = salestotal_dateyear.groupby('Date_Year').sum()
labels2=[x for x in salestotal_grp_dateyear.index]
plt.figure(figsize=(20,10))
plt.ticklabel_format(style='plain')
plt.rc('xtick', labelsize=25) 
plt.rc('ytick', labelsize=25) 
plt.bar(labels2, salestotal_grp_dateyear['Sales_Total'], align='center', color=['black', 'red', 'green', 'blue', 'cyan'])
plt.xticks(labels2,rotation=65)
plt.ylabel('total sales',size=25)
plt.title('total sales by  Month/Year ',size=25)


# In[ ]:





# # Bar Chart shows Products Cancelled by Month

# In[8]:


plt.figure(figsize=(20,10))
plt.ticklabel_format(style='plain')
cancelled = sales_data.loc[:, ['CanceledQty', 'Month']]
cancelled_grpby_month = cancelled.groupby('Month').sum() 
labels_=['January','February','March','April','May',
'June','July','August','September','October','November','December']
plt.rc('xtick', labelsize=25) 
plt.rc('ytick', labelsize=25) 
plt.bar(labels_, cancelled_grpby_month['CanceledQty'], align='center', color=['black', 'red', 'green', 'blue', 'cyan'])
plt.xticks(labels_,rotation=65)
plt.ylabel('cancelled Quantity',size=25)
plt.title('Products Cancelled by Month',size=25)
plt.show()


# In[ ]:





# # Bar Chart shows Prdoucts Cancelled by year

# In[9]:


plt.figure(figsize=(10,10))
plt.ticklabel_format(style='plain')
plt.rc('xtick', labelsize=25) 
plt.rc('ytick', labelsize=25) 
cancelled = sales_data.loc[:, ['CanceledQty', 'Year']]
cancelled_grpby_year = cancelled.groupby('Year').sum() 
labels4 = ['2010', '2011']
plt.bar(labels4, cancelled_grpby_year['CanceledQty'], color=['black', 'red'])
plt.ylabel('cancelled Quantity',size=25)
plt.title('Products Cancelled by Year',size=25)


# In[ ]:





# # Bar Chart Shows Total Sales by Month

# In[10]:


totalsales = sales_data.loc[:, ['Sales_Total', 'Month']]
totalsales_bymonth = totalsales.groupby('Month').sum()
plt.figure(figsize=(20,10))
plt.ticklabel_format(style='plain')
plt.rc('xtick', labelsize=25) 
plt.rc('ytick', labelsize=25) 
labels5=['January','February','March','April','May',
'June','July','August','September','October','November','December']
plt.bar(labels5,totalsales_bymonth['Sales_Total'], align='center', color=['black', 'red', 'green', 'blue', 'cyan'])
plt.xticks(labels5,rotation=65)
plt.ylabel('Sales Total',size=25)
plt.title('Total Sales By Month',size=25)
plt.show()


# In[ ]:





# # Bar Chart shows Total sales by Year

# In[11]:


plt.figure(figsize=(10,10))
plt.ticklabel_format(style='plain')
plt.rc('xtick', labelsize=25) 
plt.rc('ytick', labelsize=25) 
salebyyea = sales_data.loc[:, ['Sales_Total', 'Year']]
sale_grpby_year = salebyyea.groupby('Year').sum() 
labels4 = ['2010', '2011']
plt.bar(labels4, sale_grpby_year['Sales_Total'], color=['black', 'blue'])
plt.ylabel('Quantity',size=25)
plt.title('total sales by Year',size=25)


# In[ ]:





# In[ ]:




