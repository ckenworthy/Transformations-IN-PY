#!/usr/bin/env python
# coding: utf-8

# # Import data

# In[4]:


import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
from scipy.stats import boxcox


# In[17]:


cruise_ship = pd.read_csv(r"C:\Users\Camille Kenworthy\OneDrive\Desktop\aug\cruise_ship.csv")


# ## Read and View

# In[20]:


pd.options.display.max_columns = None
cruise_ship.head()


# # Exam for Normal

# In[21]:


sns.pairplot(cruise_ship)


# ## Tranform Postive SKewed Data

# In[22]:


## Tonnage


# In[23]:


cruise_ship['TonnageSQRT'] = np.sqrt(cruise_ship['Tonnage'])


# In[24]:


cruise_ship.head()


# In[25]:


cruise_ship.TonnageSQRT.hist()


# In[26]:


cruise_ship['TonnageLOG'] = np.log(cruise_ship['Tonnage'])
cruise_ship.head()


# In[27]:


cruise_ship.TonnageLOG.hist()


# ### Cabins

# In[28]:


cruise_ship['CabinsSQRT'] = np.sqrt(cruise_ship['Cabins'])
cruise_ship.head()


# In[29]:


cruise_ship.CabinsSQRT.hist()


# #### Passendges

# In[30]:


cruise_ship['passngrsSQRT'] = np.sqrt(cruise_ship['passngrs'])
cruise_ship.head()
cruise_ship.passngrsSQRT.hist()


# # CREW

# In[31]:


cruise_ship['CrewSQRT'] = np.sqrt(cruise_ship['Crew'])
cruise_ship.head()


# In[32]:


cruise_ship.CrewSQRT.hist()


# # PassSpcR

# In[33]:


cruise_ship['PassSpcRSQRT'] = np.sqrt(cruise_ship['PassSpcR'])
cruise_ship.head()


# In[34]:


cruise_ship.PassSpcRSQRT.hist()


# # OUTCAB

# In[35]:


cruise_ship['outcabSQRT'] = np.sqrt(cruise_ship['outcab'])


# In[36]:


cruise_ship.head()


# In[37]:


cruise_ship.outcabSQRT.hist()


# In[38]:


cruise_ship['outcabLOG'] = np.log(cruise_ship['outcab'])


# In[39]:


cruise_ship.head()


# In[40]:


cruise_ship.outcabLOG.hist()


# In[41]:


# Transform Negatively Skewed Data


# In[42]:


cruise_ship['YearBltSQ'] = cruise_ship['YearBlt']**2


# In[43]:


cruise_ship.head()


# In[44]:


cruise_ship.YearBltSQ.hist()


# In[45]:


cruise_ship['YearBltCUBE'] = cruise_ship['YearBlt']**3


# In[46]:


cruise_ship.head()


# In[47]:


cruise_ship.YearBltCUBE.hist()


# # Length
# Go with square, cube takes it too far

# In[49]:


cruise_ship['LengthSQ'] = cruise_ship['Length']**2


# In[50]:


cruise_ship.head()


# In[51]:


cruise_ship.LengthSQ.hist()


# In[52]:


cruise_ship['LengthCUBE'] = cruise_ship['Length']**3
cruise_ship.head()
cruise_ship.LengthCUBE.hist()


# In[ ]:




