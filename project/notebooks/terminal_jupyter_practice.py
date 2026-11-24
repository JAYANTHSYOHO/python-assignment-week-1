#!/usr/bin/env python
# coding: utf-8

# # Terminal, VS Code and Jupyter
# This notebook practises IPython timing and explains when to use notebooks or Python scripts.

# ## Notebook or Python file?
# Use a notebook to explore data step by step and show code beside its results.
# Use a notebook when charts, notes, and results should be presented together.
# Use a .py file for reusable programs, automation, and code run outside Jupyter.
# Use a .py file when you want a clear entry point for a larger application.

# ## Compare a list comprehension with a for loop
# Both approaches below create a list of squared values. %timeit runs each expression several times and reports an average.

# In[1]:


numbers = list(range(1000))

def squares_with_loop(values):
    result = []
    for value in values:
        result.append(value * value)
    return result


# In[2]:


get_ipython().run_line_magic('timeit', '[value * value for value in numbers]')


# In[3]:


get_ipython().run_line_magic('timeit', 'squares_with_loop(numbers)')

