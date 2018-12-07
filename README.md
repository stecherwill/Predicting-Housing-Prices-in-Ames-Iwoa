## Ames Housing Data and Kaggle Challenge

## Problem Statement

Want to build a regression model based on the Ames Housing Dataset. This model will predict the price of a house at sale as well as show what improvements can be made to increase the value of a home. In order to make this model I will creatively handle missing and null values. Use feature engineering to develop unique interaction terms using polynomial features. Then implement regularization to produce a quality cross value score and R2 score that will be the most efficient to predict the price of a house at sale.  


## Executive Summary
The Ames Housing dataset from 2006 to 2010 was compiled by Dean De Cock. The data set contains 2930 observations and a large number of explanatory variables (23 nominal, 23 ordinal, 14 discrete, and 20 continuous) involved in assessing home
values. Many home owners would love to be able to increase the value of their home, however accomplishing this can be much harder than it seems. Knowing the value of your home before putting it on the market is a key component. This way you would be able to figure out where your house would need improvements as to add the most value. These findings are going to help find and provide a way for homeowmners to know and increase the value of their home.


## Contents:

[Data Cleaning and EDA](./code/01_Cleanup_EDA.ipynb) 
[Preprocessing and Feature Engineering](./code/02_Preprocessing_and_Feature_Engineering.ipynb)
[Model Benchmarks](./code/03_Model_Benchmarks.ipynb) 
[Model Tuning and Predictions](./code/04_Model_Tuning_and_Predictions.ipynb)
[Production Model and Insights](./code/05_Production_Model_and_Inights.ipynb)

 
## Data Dictionary
Link to Data Description below:

[data description](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt)

## Conclusions and Recommendations


#### Overview of Investigations

The biggest takeaways were that square footage, quality, and neighborhood, are the most important predictors for sale price. While no feature out of the ones provided in the data set necessarily would decrease the value of your home, many had little to no impact. The ridge regularization regression model was used and it performs L2 regularization, i.e. adds penalty equivalent to square of the magnitude of coefficients and explains 90.27% of variability within the data.

#### Recommendationms
The key to increasing to a home is to remodel your home in all aspects. Quality is a big key predictor when determining sale price. There are many ways to accomplish this, through kitchen and basement remodels etc. Neighborhoods are the strongest predictor, before buying a house, finding the right neighborhood can make all the difference when you go to re-sell.




