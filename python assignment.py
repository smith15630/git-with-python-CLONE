#!/usr/bin/env python
# coding: utf-8

# In[3]:


# importing the dataset
import pandas
df = pandas.read_csv('regrex1.csv')
print(df)


# In[10]:


#scatterplot of data
import matplotlib.pyplot as plt
plt.scatter(df[['x']], df[['y']], color = 'red')

plt.title('y vs x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[20]:


#scatterplot of data with line


#calculate slope and intercept of regression line
def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')
slope = np.polyfit(df.x, df.y,1)[0]
intercept = np.polyfit(df.x, df.y,1)[1]
import matplotlib.pyplot as plt
import numpy as np
plt.scatter(df[['x']], df[['y']], color = 'red')
plt.title('y vs x')
plt.xlabel('x')
abline(slope, intercept)
plt.ylabel('y')
plt.show()



