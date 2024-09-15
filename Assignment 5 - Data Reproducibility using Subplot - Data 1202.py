#!/usr/bin/env python
# coding: utf-8

# In[53]:


#creating a visualization FUNCTION for average, maximum, and minimum data for datasets 1 to 4
def visualize(filename):

    #putting the dataset filename 
    data = numpy.loadtxt(fname=filename, delimiter=',') 

    #creating a figure of 10 for the weight and 3 for the height
    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    #creating a subplot with 1 row, 3 column, 3 index
    
    #first subplot: computing the average of each features
    #putting a label as AVERAGE for the y-axis and FEATURE# for the x-axis
    axes1 = fig.add_subplot(1, 3, 1) 
    
    axes1.set_ylabel('Average') 
    axes1.set_xlabel('Feature#') 
    axes1.plot(numpy.mean(data, axis=0))
    
    #second subplot: computing the maximum of each features
    #putting a label as MAX for the y-axis and FEATURE# for the x-axis
    axes2 = fig.add_subplot(1, 3, 2)
    
    axes2.set_ylabel('Max')
    axes2.set_xlabel('Features')
    axes2.plot(numpy.max(data, axis=0))
    
    #second subplot: computing the minimum of each features
    #putting a label as MIN for the y-axis and FEATURE# for the x-axis
    axes3 = fig.add_subplot(1, 3, 3)
    
    axes3.set_ylabel('Min')
    axes3.set_xlabel('Features')
    axes3.plot(numpy.min(data, axis=0))
           
    fig.tight_layout()
    matplotlib.pyplot.show()


# In[73]:


#identifying issues in the datasets
#using if elif else statement to follow the flowchart and print descrption base on the condition given
def identify_issues(filename):

    data = numpy.loadtxt(fname=filename, delimiter=',')

    if numpy.max(data, axis=0)[0] == 0 and numpy.max(data, axis=0)[20] == 20:
        print('I doubt the integrity of this dataset\n')
    elif any(numpy.min(data, axis=0)) == 0:
        print('Why is this happening\n')
    else:
        print('Dataset looks good\n')
   


# In[74]:


#importing libraries and loading datasets
import glob
import numpy 
import matplotlib
import matplotlib.pyplot 

dataset = sorted(glob.glob('data*.csv'))

for datasets in dataset[:4]:
    print(datasets)
    visualize(datasets)
    identify_issues(datasets)


# In[ ]:


#Thank you so much

