
# coding: utf-8

# # Prerequisite SG Computing Laboratory Batch II 2019
# 
# These notebook is to answer some questions about a very first step to be a data scientist. After answering these questions, we hope that you will be more familiar with `pandas` and visualize the data provided.
# 
# References:
# - [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
# - [Pandas Visualization](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)
# 
# 
# ## Pandas
# We will start off by using a powerful Python data analysis library by the name of `pandas`. To install `pandas` pip and conda can be used
# 
# ```{python}
# pip install pandas
# or
# conda install pandas
# ```

# In[3]:


# import the library here
import pandas as pd


# Let's start with reading our first dataset, `bank-full.csv`. The dataset is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be (or not) subscribed. The classification goal is to predict if the client will subscribe a term deposit (variable y).
# 
# Attribute information:
#    
# `age`
# 
# `job` : type of job
# 
# `marital` : marital status
# 
# `education`
# 
# `default`: has credit in default?
# 
# `balance`: average yearly balance, in euros 
# 
# `housing`: has housing loan?
# 
# `loan`: has personal loan?
#    
# `contact`: contact communication type
# 
# `day`: last contact day of the month (numeric)
# 
# `month`: last contact month of year
# 
# `duration`: last contact duration, in seconds
# 
# `campaign`: number of contacts performed during this campaign and for this client
# 
# `pdays`: number of days that passed by after the client was last contacted from a previous campaign (-1 means client was not previously contacted)
# 
# `previous`: number of contacts performed before this campaign and for this client
# 
# `poutcome`: outcome of the previous marketing campaign
# 
# `y`: has the client subscribed a term deposit?

# In[4]:


# load the dataset here and assign it into a variable called 'bank'
bank = pd.read_csv('bank-full.csv')


# In[5]:


bank.info()


# if you have no idea about the data, you can use `.head()` to show first five rows of the data or you can use `.tail()` to show 5 last five rows of the data

# In[6]:


# show first or last five rows of the data
bank.tail()


# But how about the size of our dataset? To get that information we can use `.shape` to show how many rows and columns that our data have

# In[10]:


# get the size of our data
bank.shape


# The results of our code above will be in `(x, y)` format. `x` means how many rows that our data have and `y` means how many columns/atribute/feature that our data have.
# 
# Since we have `y` columns, we still don't know what is the data type of our columns. To show all columns and each data types we can use `.dtypes`. Let's try it below.

# In[13]:


# Your code here
bank.dtypes


# As you can see there's so many objects in our data. For example there's a `education` column, but how many unique values and it's distribution in `education` column? You can use `.value_counts()`. If we want to show the precentage, we can pass a paratameter `normalize=True` in `.value_counts()`. Please show us the distribution of unique values in `education` column.

# In[14]:


# Your code here
bank.education.value_counts()


# ## Data Visualization
# 
# Data visualization is the discipline of trying to understand data by placing it in a visual context so that patterns, trends and correlations that might not otherwise be detected can be exposed.
# Python offers multiple great graphing libraries that come packed with lots of different features. No matter if you want to create interactive, live or highly customized plots python has an excellent library for you.
# To get a little overview here are a few popular plotting libraries:
# - Matplotlib: low level, provides lots of freedom
# - Pandas Visualization: easy to use interface, built on Matplotlib
# - Seaborn: high-level interface, great default styles
# - ggplot: based on R’s ggplot2, uses Grammar of Graphics
# - Plotly: can create interactive plots
# 
# For answering the questions you just need `pandas`, so you don't to install another tools but if you want to install it's great!.
# 
# Plotting methods allow for a handful of plot styles other than the default line plot. These methods can be provided as the kind keyword argument to `plot()`, and include:
# 
# - ‘bar’ or ‘barh’ for bar plots
# - ‘hist’ for histogram
# - ‘box’ for boxplot
# - ‘kde’ or ‘density’ for density plots
# - ‘area’ for area plots
# - ‘scatter’ for scatter plots
# - ‘hexbin’ for hexagonal bin plots
# - ‘pie’ for pie plots
# 
# The plot method on Series and DataFrame is just a simple wrapper around `plt.plot()`

# ## Questions
# 
# 1. How is the correlation between `balance` and `age`? You can use scatter plot to show the relationship. Scatter plot might be one of the most used types of plot in understanding the distribution between numeric data.

# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


# Your code here
bank.plot.scatter(x='age', y='balance')


# Dari plot di atas, terlihat hampir tidak ada korelasi di antara age dan balance. Karena pergerakan (berkurang atau bertambah-nya) angka age tidak mempengaruhi pergerakan angka balance. 
# 
# Namun, dari plot di atas terlihat bahwa balance tersebar banyak di range <= 20000 untuk semua range age. 

# In[17]:


bank[bank.balance <= 20000].plot.scatter(x='age', y='balance')


# In[26]:


(bank.balance[bank.balance <= 20000].count()) / bank.shape[0] * 100


# Sekitar 99.57% client memiliki balance di range <= 20000. 

# 2. A bar plot is fundamentally the plot to compare different group of data. Using bar plot show us category comparison using bar plot in `job` column.

# In[27]:


bank.job.value_counts().plot.bar()


# 3. How is the percentage of marital status in our data? You can use pie plot or bar plot but give us a reason why you use that chart

# Pie chart lebih cocok dipakai jika ingin melihat persentase. Karena semua kategori berada dalam satu 'pie' sehingga proporsi tiap kategori terhadap keseluruhannya terlihat jelas. 

# In[28]:


# Your code here
bank.marital.value_counts().plot.pie(labels=['Married', 'Single', 'Divorce'], colors=['r', 'g', 'b'],autopct='%.2f', fontsize=10, figsize=(4, 4))


# 4. Boxplot is summary of sample distribution that presented graphically that can describe the form of data distribution (skewness), the size of the central tendency and the size of the spread (diversity) of observational data. Show us the box plot of `duration`. Is there an outlier or extreme value in `duration` column?

# ya, ada banyak nilai outlier dan extreme, terlihat dari boxplot. 

# In[30]:


# Your code here
bank.duration.plot.box()


# In[31]:


bank.duration.describe()

