#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt 


# In[5]:


file=pd.read_csv("Superstore.csv")


# In[6]:


file


# In[27]:


customer_count = len(file["Order ID"].unique())

print("Number of customers:",customer_count)


# In[31]:


segments=file["Segment"].value_counts()

print(segments)


# In[35]:


shipmode=file["Ship Mode"].value_counts()

print(shipmode)


# In[42]:


TotalSales=file["Sales"].sum()

print("Total Sales: ",TotalSales)


# In[45]:


Profit=file["Profit"].sum()

print("Total Profit: ",Profit)


# In[47]:


Discount=file["Discount"].sum()

print("Total Discount: ",Discount)


# In[97]:


shipmode=file["Ship Mode"].value_counts()

print(shipmode)

plt.figure(figsize=(6,5))
plt.bar(shipmode.index, shipmode.values,color=['skyblue','grey'])
plt.xlabel('Ship Mode')
plt.ylabel('Counts')
plt.title('Ship Mode Distribution')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom')

plt.show()


# In[90]:


Sub_Category_Counts= file['Sub-Category'].value_counts()

plt.figure(figsize=(4,4))

ax=plt.axes()
ax.set_facecolor('orange')

plt.pie(Sub_Category_Counts, labels=Sub_Category_Counts.index,colors = ['#8c564b', '#bd9e77', '#d8b892', '#e4cba4', '#f2d5b0'],shadow=True)
plt.title('Sub-Category')
plt.show()

print(Sub_Category_Counts)


# In[20]:


Category_Counts= file['Category'].value_counts()

plt.figure(figsize=(4,4))

ax=plt.axes()
ax.set_facecolor('orange')

plt.pie(Category_Counts, labels=Category_Counts.index,autopct='%1.1f%%', startangle=60,explode=(0,0.050,0),shadow=True,colors=['grey', 'yellow','lightblue'])
plt.title('Sub-Category')
plt.show()

print(Category_Counts)


# In[38]:


top_10_Sales= file.sort_values(by='Quantity', ascending=False).head(6)

x = top_10_Sales["Sales"]
y = top_10_Sales["Profit"]

plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Top 10 Quantity and Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.title('Top 10 Sales and Profit - Line Chart')
plt.legend()
plt.grid(True)
plt.show()


# In[31]:


top_10_city = file.groupby('City')['Sales'].sum().nlargest(10)

x = top_10_city.index
y = top_10_city.values

plt.figure(figsize=(10, 6))
ax = plt.axes()
ax.set_facecolor('skyblue')

plt.barh(x, y, color='blue')
plt.xlabel('Sales')
plt.ylabel('City')
plt.title('Top 10 Cities by Sales')
plt.show()


# In[76]:


top10_city=file.groupby("City")['Profit'].sum().nlargest(10)


x = top10_city.index
y = top10_city.values

plt.figure(figsize=(11,6))
ax = plt.axes()
ax.set_facecolor('yellow')

plt.bar(x, y, color='skyblue')
plt.xlabel('Profit')
plt.ylabel('City')
plt.title('Top 10 Cities by Profit')
plt.legend("city")

plt.show()


# In[91]:


Category_Profit=file.groupby("Category")['Profit'].sum().nlargest(10)


x = Category_Profit.index
y = Category_Profit.values

plt.figure(figsize=(6,6))
ax = plt.axes()
ax.set_facecolor('skyblue')

plt.bar(x, y, color='red')
plt.xlabel('Category')
plt.ylabel('Profit')
plt.title("category wise Profit")
plt.legend("city")
plt.show()


# In[95]:


Category_Sales=file.groupby("Category")['Sales'].sum().nlargest(20)


x = Category_Sales.index
y = Category_Sales.values

plt.figure(figsize=(8,5))
ax = plt.axes()
ax.set_facecolor('lightgreen')

plt.barh(x, y, color='orange')
plt.ylabel('Category')
plt.xlabel('Profit')
plt.title("category wise Sales")
plt.legend("city")
plt.show()


# In[115]:


x = file["Quantity"].head(10)
y = file["Profit"].head(10)

plt.figure(figsize=(5,5))
plt.plot(x, y, marker='o', linestyle='-', color='b', label='range')
plt.xlabel('Quantity')
plt.ylabel('Profit')
plt.title('Line Chart Example')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




