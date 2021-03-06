#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random

# this will choose one and remove it
def choose_and_remove(items):
    # pick an item index
    if items:
        index = random.randrange( len(items) )
        return items.pop(index)
    # nothing left!
    return None

def get_max_list(l, allowed_actions):
    index=None
    if (len(allowed_actions)==2):
        new_actions=[l[0],l[2]]
        if(new_actions[0]==new_actions[1]):
            index=random.sample([0,2],1)[0]
        elif (new_actions[0]>new_actions[1]):
            index=0
        else :
            index=2
    elif(len(allowed_actions)==3):
        if (l[0]==l[1] and l[1]==l[2]):
            index=random.sample([0,1,2],1)[0]
        elif (l[0]>=l[1]):
            if(l[0]==l[2]):
                index=random.sample([0,2],1)[0]
            elif (l[0]> l[2]):
                index=0
            else:
                index=2
        elif(l[0]<=l[1]):
            if(l[1]==l[2]):
                index=random.sample([1,2],1)[0]
            elif (l[1]>l[2]):
                index=1
            else:
                index=2
    return(index)


# In[ ]:




