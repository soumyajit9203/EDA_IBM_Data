#!/usr/bin/env python
# coding: utf-8

# # Explanatory Data Analysis on IBM Employee Attrition.

# In this is project on we are going to work on IBM Employee Attrition dataset. At first we have to import some libraries 
# to load the dataset and Analysis the dataset.

# In[15]:


# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[16]:


#load data set 
df=pd.read_csv("IBM.csv")


# The data set contains 13 columns and 1470 rows. There is the glimpse of the data set below.
# 

# In[17]:


# A glimpse of the data set 
df.head()
df


# In[18]:


#Checking Missing Values 
df.isnull().sum()


# We can see that there is no missing values in each columns . Therefore we have total 19110 observations in the dataset .

# In[19]:


#checking the datatypes
df.dtypes


# To do the Analysis in a better way or get some more information from the given data set , we will add some columns by recoding the previous colmuns like Education ,EnvironmentSatisfaction, JobSatisfaction, WorkLifeBalance.For example 
# Education: 1-Below College; 2- College; 3-Bachelor; 4-Master; 5-Doctor 
# EnvironmentSatisfaction: 1-Low; 2-Medium; 3-High; 4-Very High 
# JobSatisfaction: 1-Low; 2-Medium; 3-High; 4-Very High
# WorkLifeBalance: 1-Bad; 2-Good; 3-Better; 4-Best

# In[20]:


df["Education_C"]=0
for i in range(len(df)):
    if   df["Education"][i] ==1 :
         df["Education_C"][i]="Low"
    elif df["Education"][i] ==2 :
         df["Education_C"][i]="Medium"
    elif df["Education"][i] ==3 :
         df["Education_C"][i]="High"
    elif df["Education"][i] ==4 :
         df["Education_C"][i]="Very High"
    else :
         df["Education_C"][i]="exellent"


# In[21]:


df["EnvironmentSatisfaction_C"]=0
for i in range(len(df)):
    if   df["EnvironmentSatisfaction"][i] ==1 :
         df["EnvironmentSatisfaction_C"][i]="Low"
    elif df["EnvironmentSatisfaction"][i] ==2 :
         df["EnvironmentSatisfaction_C"][i]="Medium"
    elif df["EnvironmentSatisfaction"][i] ==3 :
         df["EnvironmentSatisfaction_C"][i]="High"
    elif df["EnvironmentSatisfaction"][i] ==4 :
         df["EnvironmentSatisfaction_C"][i]="Very High"
    else :
         df["EnvironmentSatisfaction_C"][i]="exellent"


# In[22]:


df["JobSatisfaction_C"]=0
for i in range(len(df)):
    if   df["JobSatisfaction"][i] ==1 :
         df["JobSatisfaction_C"][i]="Low"
    elif df["JobSatisfaction"][i] ==2 :
         df["JobSatisfaction_C"][i]="Medium"
    elif df["JobSatisfaction"][i] ==3 :
         df["JobSatisfaction_C"][i]="High"
    elif df["JobSatisfaction"][i] ==4 :
         df["JobSatisfaction_C"][i]="Very High"
    else :
         df["JobSatisfaction_C"][i]="exellent"


# In[23]:


df["WorkLifeBalance_C"]=0
for i in range(len(df)):
    if   df["WorkLifeBalance"][i] ==1 :
         df["WorkLifeBalance_C"][i]="Low"
    elif df["WorkLifeBalance"][i] ==2 :
         df["WorkLifeBalance_C"][i]="Medium"
    elif df["WorkLifeBalance"][i] ==3 :
         df["WorkLifeBalance_C"][i]="High"
    elif df["WorkLifeBalance"][i] ==4 :
         df["WorkLifeBalance_C"][i]="Very High"
    else :
         df["WorkLifeBalance_C"][i]="exellent"


# In[24]:


# The glimpse of the dataset after the adding the new colmuns 
df


# In[25]:


#Summary of the data set for numerical variables 
df.describe()


# In[26]:


# We will Calculate the Correlation between the variables .
df.corr()


# In[27]:


## Diagrammatic representation of correlations between the variables
sns.heatmap(df.corr(), fmt='.1f', annot=True, cmap= "bone_r")
plt.title('Correlation between variables')


# In[31]:


data1=df["Age"]
plt.subplot(2,2,1)
plt.violinplot(data1,vert=True)
plt.title("violinplot of Age")
data2=df["MonthlyIncome"]
plt.subplot(2,2,2)
plt.violinplot(data2,vert=True)
plt.title("violinplot of MonthlyIncome")
data3=df["NumCompaniesWorked"]
plt.subplot(2,2,3)
plt.violinplot(data1,vert=True)
plt.title("violinplot of NumCompaniesWorked")
data4=df["YearsAtCompany"]
plt.subplot(2,2,4)
plt.violinplot(data1,vert=True)
plt.title("violinplot of Years At Company")
plt.show()


# From the violin of the numerical variables that is Age, Monthly Income , Num of companies worked, Years at company , we can see that there is no outliers values in Age, Num of companies worked, Years at company .But There a lot of outliers in the Monthly Income .

# In[34]:


#Age attrition of employees
sns.countplot(data = df,x=df['Age'],hue="Attrition",palette='ocean')
plt.title('Age distribution of Employees')


# In[27]:


# Departmental Attrition of Employees
df['Department'].value_counts()


# In[26]:


sns.countplot(data = df,x=df['Department'])
plt.title('Departmental Attrition of Employees')


# In[25]:


# # Attrition for left Employees
df['Attrition'].value_counts()


# In[24]:


# # Attrition for left Employees
sns.countplot(data = df,x=df['Attrition'])
plt.title(' Attrition for left Employees')


# In[29]:


#Attrition by EducationField
df['EducationField'].value_counts()


# In[31]:


sns.countplot(data = df,x=df['EducationField'])
plt.title('Attrition by EducationField')


# In[32]:


## number of married and unmarried employees
df["MaritalStatus"].value_counts()


# In[33]:


sns.countplot(data = df,x=df['MaritalStatus'])
plt.title('MaritalStatus of the employees')


# In[16]:


# Attrition by Education
df['Education_C'].value_counts()
sns.countplot(data = df,x=df['Education_C'])
plt.title('Education Attrition of Employees')


# In[17]:


# Attrition by EnvironmentSatisfaction
df['EnvironmentSatisfaction_C'].value_counts()
sns.countplot(data = df,x=df['EnvironmentSatisfaction_C'])
plt.title('EnvironmentSatisfaction Attrition of Employees')


# In[18]:


# Attrition by JobSatisfaction
df['JobSatisfaction_C'].value_counts()
sns.countplot(data = df,x=df['JobSatisfaction_C'])
plt.title('JobSatisfaction Attrition of Employees')


# In[19]:


# Attrition by WorkLifeBalance
df['WorkLifeBalance_C'].value_counts()
sns.countplot(data = df,x=df['WorkLifeBalance_C'])
plt.title('WorkLifeBalance Attrition of Employees')


# 
