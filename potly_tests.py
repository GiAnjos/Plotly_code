#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import plotly.express as px

mc_menu = pd.read_csv('India_Menu.csv')


# In[17]:


mc_menu.head()


# In[18]:


# Create the line graph
line_graph = px.line(
  # Set the appropriate DataFrame and title
  data_frame=mc_menu, title='Total of Sugar per item', 
  # Set the x and y arguments
  x='Menu Items', y='Total Sugars (g)')

line_graph.show()


# In[22]:


# Create the bar graph object
bar_fig = px.bar(
  # Set the DataFrame, x and y
  data_frame=mc_menu, x='Menu Items', y='Protein (g)')
  # Set the graph to be horizontal
  #orientation='h', title='Total of protein per items')

# Increase the gap between bars
bar_fig.update_layout({'bargap': 0.5})

bar_fig.show()


# In[ ]:




