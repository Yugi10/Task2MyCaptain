#!/usr/bin/env python
# coding: utf-8

# In[21]:


n = int(input ("How many elements do you want in your list ?\n "))
list =  []
output = []

for i in range (1,n+1) :
    element = int(input ("\nPlease enter the element number " + str(i) + " of the list :\n"))
    list.append(element)
    
print ("\nYour list is :\n" ,list)

for a in range (0,n) :
    
    if list [a] >= 0 :
        output.append(list [a])
    
    else :
        continue
        
print ("\nYour list with only positive elements is :\n" ,output)

