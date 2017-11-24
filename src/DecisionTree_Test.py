
# coding: utf-8

# In[94]:


import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import gzip
import pickle


# In[95]:


import scipy as sp


# In[96]:


with gzip.open(r'../data/LibData.pkl.gz') as f:
    utilization = pickle.load(f)


# In[97]:


attData = pd.read_csv(r'../data/computerAttributes.csv',header=0)


# In[98]:


attData.head()


# In[99]:


attData.index = attData['computerName']
attData.head()


# In[100]:


utilization.head()


# # Testing the last 3 years (Fall 14 - Spring 17)

# In[101]:


#Split into semesters

#spring2010 = utilization[(utilization.index >= '2010-01-19') & (utilization.index < '2010-05-12')]
#summer2010 = utilization[(utilization.index >= '2010-05-17') & (utilization.index < '2010-08-09')]
#fall2010 = utilization[(utilization.index >= '2010-08-23') & (utilization.index < '2010-12-15')]

#spring2011 = utilization[(utilization.index >= '2011-01-10') & (utilization.index < '2011-05-04')]
#summer2011 = utilization[(utilization.index >= '2011-05-12') & (utilization.index < '2011-08-08')]
#fall2011 = utilization[(utilization.index >= '2011-08-22') & (utilization.index < '2011-12-13')]

#spring2012 = utilization[(utilization.index >= '2012-01-09') & (utilization.index < '2012-05-02')]
#summer2012 = utilization[(utilization.index >= '2012-05-14') & (utilization.index < '2012-08-06')]
#fall2012 = utilization[(utilization.index >= '2012-08-20') & (utilization.index < '2012-12-14')]

#spring2013 = utilization[(utilization.index >= '2013-01-14') & (utilization.index < '2013-05-08')]
#summer2013 = utilization[(utilization.index >= '2013-05-13') & (utilization.index < '2013-08-05')]
#fall2013 = utilization[(utilization.index >= '2013-08-19') & (utilization.index < '2013-12-12')]

#spring14 = utilization[(utilization.index >= '2014-01-13') & (utilization.index < '2014-05-07')]
#summer14 = utilization[(utilization.index >= '2014-05-12') & (utilization.index < '2014-08-05')]

fall14 = utilization[(utilization.index >= '2014-08-18') & (utilization.index < '2014-12-12')]
spring15 = utilization[(utilization.index >= '2015-01-12') & (utilization.index < '2015-05-06')]
summer15 = utilization[(utilization.index >= '2015-05-11') & (utilization.index < '2015-08-03')]
fall15 = utilization[(utilization.index >= '2015-08-17') & (utilization.index < '2015-12-11')]
spring16 = utilization[(utilization.index >= '2016-01-11') & (utilization.index < '2016-05-04')]
summer16 = utilization[(utilization.index >= '2016-05-09') & (utilization.index < '2016-08-05')]
fall16 = utilization[(utilization.index >= '2016-08-22') & (utilization.index < '2016-12-16')]
spring17 = utilization[(utilization.index >= '2017-01-17') & (utilization.index < '2017-05-10')]
summer17 = utilization[(utilization.index >= '2017-05-15') & (utilization.index < '2017-08-07')]


# In[102]:


#semesters = [fall2011, spring2012, summer2012, fall2012, spring2013, summer2013, fall2013, spring14, summer14, fall14, spring15, summer15, fall15, spring16, summer16, fall16, spring17, summer17]
semesters3 = [fall14, spring15, summer15, fall15, spring16, summer16, fall16, spring17, summer17]
semesters1 = [spring16, summer16, fall16, spring17, summer17]


# In[103]:


#utilization2 = pd.concat(semesters)

utilization2 = pd.concat(semesters3)
utilization4 = utilization2.mean()

attData['utilizationMean'] = utilization4.values


# In[104]:


attData.head()


# In[105]:


attData.shape


# In[106]:


# Only want the machines that require a logon
attData1 = attData[attData['requiresLogon'] != 0]


# In[107]:


attData2 = attData1[attData1['isDesktop'] != 0]


# In[108]:


attData1[attData1['location'] == 'na']


# In[109]:


attData2[attData2['location'] == 'na']


# In[110]:


attData1 = attData1[attData1['computerName'] != 'LIBFALL17']


# In[111]:


attData2 = attData2[attData2['computerName'] != 'LIBFALL17']


# In[112]:


attData1.shape


# In[113]:


attData2.shape


# In[114]:


#attData1.loc[attData1['utilizationMean'].idxmin()]


# In[115]:


dataM = attData1['utilizationMean']

five_num = [dataM.quantile(0),   
            dataM.quantile(0.25),
            dataM.quantile(0.50),
            dataM.quantile(0.75),
            dataM.quantile(1)]

High = dataM.quantile(0.75)

five_num


# In[116]:


dataM2 = attData2['utilizationMean']

five_num2 = [dataM2.quantile(0),   
            dataM2.quantile(0.25),
            dataM2.quantile(0.50),
            dataM2.quantile(0.75),
            dataM2.quantile(1)]

High2 = dataM2.quantile(0.75)

five_num2


# In[117]:


# .25 - .3 gives Accuracy Score of 88% - 90% !!!!!!
#attData1['Label'] = attData1['utilizationMean'].map(lambda x: "Low" if x < .28 else "High")

# gives Accuracy Score of 71% - 72%
attData1['Label'] = attData1['utilizationMean'].map(lambda x: "Low" if x < High else "High")
attData1.head()


# In[118]:


attData2['Label'] = attData2['utilizationMean'].map(lambda x: "Low" if x < High2 else "High")
attData2.head()


# In[119]:


attData1 = attData1.dropna() 


# In[120]:


attData2 = attData2.dropna() 


# In[121]:


attData1.iloc[:, [3,4,5,6,7,8,9,10,11,12,13]].head()


# In[122]:


attData1.iloc[:, [15]].head()


# In[123]:


#attData1[attData1['floor'] == 'na']


# In[124]:


attData1.dtypes


# In[125]:


attData2.dtypes


# In[126]:


attData1.location.unique()


# In[127]:


attData2.location.unique()


# In[128]:


# Map Location to int

locationMap = {'Tower':1, 'CITI Lab':2, 'Reading Room':3, 'DMC':4, 'Info Commons':5, 'Checkout Desk':6, 'Music Library':7, 'RIS':8}

attData1['location'] = attData1['location'].map(lambda x: locationMap.get(x) if x in locationMap else x)


# In[129]:


# Map Location to int

#locationMap = {'Tower':1, 'CITI Lab':2, 'Reading Room':3, 'DMC':4, 'Info Commons':5, 'Checkout Desk':6, 'Music Library':7, 'RIS':8}

attData2['location'] = attData2['location'].map(lambda x: locationMap.get(x) if x in locationMap else x)


# In[130]:


attData1.head()


# In[131]:


attData2.head()


# In[132]:


from pandas.api.types import is_numeric_dtype
is_numeric_dtype(attData1['floor'])


# In[133]:


from pandas.api.types import is_numeric_dtype
is_numeric_dtype(attData2['floor'])


# In[ ]:





# In[134]:


attData1.floor.unique()


# In[135]:


attData2.floor.unique()


# In[136]:


attData1[attData1['floor'] == 'na'].shape


# In[137]:


# Give 'na' a value of 20 
# Convert column to int

attData1['floor'] = attData1['floor'].replace('na', 20)


# In[138]:


attData1['floor'] = attData1['floor'].astype(int)


# In[139]:


attData2['floor'] = attData2['floor'].astype(int)


# In[140]:


attData1.floor.unique()


# In[141]:


attData2.floor.unique()


# In[142]:


from pandas.api.types import is_numeric_dtype
is_numeric_dtype(attData1['floor'])


# In[143]:


from pandas.api.types import is_numeric_dtype
is_numeric_dtype(attData2['floor'])


# In[144]:


attData1.dtypes


# In[145]:


attData2.dtypes


# In[146]:


attData1.utilizationMean.hist(bins=20)
plt.show()


# In[147]:


attData2.utilizationMean.hist(bins=20)
plt.show()


# In[148]:


attData1.utilizationMean.std()


# In[149]:


attData2.utilizationMean.std()


# In[150]:


attData1[attData1['Label'] == 'Low'].shape


# In[151]:


attData2[attData2['Label'] == 'Low'].shape


# In[152]:


attData1.location.unique()


# In[153]:


attData2.location.unique()


# In[154]:


attData2.isDesktop.unique()


# In[155]:


attData2.iloc[:, [4,5,6,7,8,9,10,11,12,13]].head()


# In[156]:


from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree


# ## Running models on original data

# ### Decision Tree Model

# In[157]:


# X is the computer attributes
# Y is the outcome variable, Setting this as High or Low 

X = attData1.values[:, [3,4,5,6,7,8,9,10,11,12,13]]
Y = attData1.values[:, [15]]


# In[158]:


# split data into training and test sets 70/30

X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)


# In[159]:


# Decision tree classifier with criterion gini index

clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)


# In[160]:


# Decision tree classifier with criterion information gain

clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)


# In[161]:


#X_test[0]


# In[162]:


# Try to predict using test set first record

#clf_gini.predict([[1, 1, 3, 0, 1, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0]])


# In[163]:


#Prediction for Decision Tree classifier with criterion gini index

y_pred = clf_gini.predict(X_test)
y_pred


# In[164]:


#Prediction for Decision Tree classifier with criterion as information gain

y_pred_en = clf_entropy.predict(X_test)
y_pred_en


# In[165]:


# Accuracy Score for the Decision Tree classifier with criterion as gini index

print "Accuracy is ", accuracy_score(y_test,y_pred)*100


# In[166]:


# Accuracy Score for the Decision Tree classifier with criterion as information gain

print "Accuracy is ", accuracy_score(y_test,y_pred_en)*100


# ### Random Forest Model

# In[167]:


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# In[168]:


clf = RandomForestClassifier()
trained_model = clf.fit(X_train, y_train)
print "Trained model : ", trained_model

predictions = trained_model.predict(X_test)
 
for i in xrange(0, 5):
    print "Actual outcome :: {} and Predicted outcome :: {}".format(list(y_test)[i], predictions[i])


# In[169]:


print "Train Accuracy :: ", accuracy_score(y_train, trained_model.predict(X_train))*100
print "Test Accuracy  :: ", accuracy_score(y_test, predictions)*100
 


# In[170]:


print "Confusion matrix \n", confusion_matrix(y_test, predictions)


# ## Running models on data without laptops, possibly other skewed data

# ### Decision Tree Model 2

# In[171]:


# X is the computer attributes
# Y is the outcome variable, Setting this as High or Low 

W = attData1.values[:, [4,5,6,7,8,9,10,11,12,13]]
Z = attData1.values[:, [15]]


# In[172]:


# split data into training and test sets 70/30

W_train, W_test, z_train, z_test = train_test_split( W, Z, test_size = 0.3, random_state = 100)


# In[173]:


# Decision tree classifier with criterion gini index

clf_gini2 = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=3, min_samples_leaf=5)
clf_gini2.fit(W_train, z_train)


# In[174]:


# Decision tree classifier with criterion information gain

clf_entropy2 = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=5)
clf_entropy2.fit(W_train, z_train)


# In[175]:


#Prediction for Decision Tree classifier with criterion gini index

z_pred = clf_gini2.predict(W_test)
z_pred


# In[176]:


#Prediction for Decision Tree classifier with criterion as information gain

z_pred_en = clf_entropy2.predict(W_test)
z_pred_en


# In[177]:


# Accuracy Score for the Decision Tree classifier with criterion as gini index

print "Accuracy is ", accuracy_score(z_test,z_pred)*100


# In[178]:


# Accuracy Score for the Decision Tree classifier with criterion as information gain

print "Accuracy is ", accuracy_score(z_test,z_pred_en)*100


# In[ ]:





# ### Random Forest Model 2

# In[179]:


clf2 = RandomForestClassifier()
trained_model2 = clf2.fit(W_train, z_train)
print "Trained model : ", trained_model2

predictions2 = trained_model2.predict(W_test)
 
for i in xrange(0, 5):
    print "Actual outcome :: {} and Predicted outcome :: {}".format(list(z_test)[i], predictions2[i])


# In[180]:


print "Train Accuracy :: ", accuracy_score(z_train, trained_model2.predict(W_train))*100
print "Test Accuracy  :: ", accuracy_score(z_test, predictions2)*100
 


# In[181]:


print "Confusion matrix \n", confusion_matrix(z_test, predictions2)


# In[ ]:




