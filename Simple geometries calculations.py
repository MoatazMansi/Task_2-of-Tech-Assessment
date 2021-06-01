#!/usr/bin/env python
# coding: utf-8

# ### Prepare the package 

# In[1]:


#conda install shapely


# ### Importing libraries

# In[2]:


## for manipulation of geometric shapes
#! pip install shapely
from shapely.geometry import Polygon
from shapely import geometry
##to converting objects into a byte stream to store it in a file
import pickle


# ### Create simple polygon files

# In[3]:


# Let's create twe polygons
# cors of the first polygon 
a = [(75, 30),(85, 30),(75, 10)]
# cors of the second polygon 
b = [(82,32.261),(79.304,32.474),(77.282,30.261),(81,28)]
# creat polygong using polygon fn
polygon1 = geometry.Polygon(a)
polygon2 = geometry.Polygon(b)
# compile poygons into dic
my_polygons_ = {"polygon1":geometry.Polygon(a), "polygon2":geometry.Polygon(b)}


# In[11]:


## let's view pour polygons
polygon1


# In[13]:


polygon2


# In[4]:


## this code to Save polygons as a file to disk
## with open('./Polygon_files', "wb") as poly_file:
    #pickle.dump(Polygon_files, poly_file)


# In[5]:


## this code to Load polygon from disc
## with open('./Polygon_files', "rb") as poly_file:
    #my_polygons_ = pickle.load(poly_file)


# In[6]:


## inster the file name
##file_name = my_polygons_


# ### Implement simple polygon calculations

# In[9]:


## loop for to run simple calculations for polygons in a file 
for key in my_polygons_.keys():
    print (f"{key} is of type:", my_polygons_[key].geom_type)
    print (f"The center point of {key} is:", my_polygons_[key].centroid)
    print (f"The center point of {key} is:", my_polygons_[key].bounds)
    print (f"The center point of {key} is:", my_polygons_[key].area)

