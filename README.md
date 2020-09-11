# tester3

This is a testing applictaion.


The most important aspect of **Data Wrangling** is to clean or transform the data, preparing it for analysis. One main issue is having missing data while conducting the analysis, which can **skew or bias** results. 

The first thing to do is to always identify the **missing value**s within the dataset [link](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.isnull.html).
Once you have found the missing data, you can do the following.

* If there are columns with a few rows of missing data, the Dropna method [link](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dropna.html) could be used to drop the missing rows. 

* If there are rows with missing data, the Fillna method [link]( http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.fillna.html) can be used instead of dropping them completely. 

*Note: This method can vary with the data and the project.*


