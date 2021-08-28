# Predicting the S&P 500


### Table of Contents

- Background
- Approach Overview
- The Data
- EDA and Modeling
- Classification and Modeling using no text data
- Regression Modeling using text data
- Classification and Regression Modeling using no text data
- Results
- Conclusions
- Future Recs

## Background

This analysis is being performed by three friends that want to supplement their incomes as data scientists in the S&P 500. With mad data wizardry skills,  the three scientists will evaluate if using news from the New York Times (NYT) can increase their ability to predict market movement in the S&P 500, giving them a trading advantage. 

We came to this question when trying to tackle this problem. Is it possible that sentiment analysis on business articles coupled with other natural language processing (NLP) techniques predict S&P 500 price data with greater than 50% accuracy?

### Approach Overview:
- Used NYT API and S&P 500 to gather 10 years of data
- Cleaned and filtered data to key components
- Performed extensive EDA on both S&P 500 and NYT text data
- Parallelization of regression & classification modeling
- Compare top performing models

Software requirements: Pandas, Scikit-learn, Tenserflow, Numpy, and Matplotlib.


## The Data
Data sources:
10 years of New York Times articles (2011-2021)
10 years of S&P 500 data from Yahoo Finance

In order to acquire NYT data used an API (source: 
Forked and customized a version of pynytimes in order to access the API (source: https://github.com/michadenheijer/pynytimes). Ten articles per day for 10 years (2011-2021) were gathered from the business section of the NYT.

To gather relevant S&P 500 data:
Used Yahoo Finance (source: https://pypi.org/project/fix-yahoo-finance/0.1.30/).

Feature Selection:
- Identified relevant data from API (text and date)
- Merged all text features (heading, lead paragraph, and abstract)

Feature Engineering:
- Percent change in price
- Direction of change
- Added day of the week and holidays

Feature Cleaning:
- Removing text issues of http, punctuation, URL, and @

## EDA and Modeling
In order to ascertain the strongest relationships between data and price prediction the group decided to distribute the modeling tasks into three buckets: classification with text data, regression with text data, and both classification and regression modeling using no text data.

The goal of the multi-classification problem was to predict if price the following day will go down, up, or stay the same. Accuracy will be the metric used to verify models and compare them. The baseline accuracy score: 38.01%.

Since accuracy is a measure for classification, the goal of the regression models was to reduce MSE and MAE to establish a basic relationship between text sentiment and the movement of the S&P 500. The error scores were produced using a GridSearch, producing best parameters for measurement of the relationship.

Mean square error (MSE) is the average of the square of the errors. The larger the number the larger the error. MSE is an error metric, i.e. the lower the better.

Mean Absolute Error (MAE). MAE is simply, as the name suggests, the mean of the absolute errors. The absolute error is the absolute value of the difference between the forecasted value and the actual value. MAE tells us how big of an error we can expect from the forecast on average. MAE is an error metric, i.e. the lower the better.

https://stackoverflow.com/questions/45627784/unable-to-obtain-accuracy-score-for-my-linear

Collaborated test size of 20%, equivalent to 2 years of data for testing.


### Classification and Modeling using text data
In order to properly analyze the text multiple approaches were used. Two different types of sentiment analysis were incorporated, Vader and TextBlob. Ultimately both were incorporated to enhance the capture of sentiment. Two different types of vectorizing was used, CountVectorizing (CV) and TFIDF. The TFIDF performed the best from the multiple models tested and was the designated tokenizer for the rest of the modeling.

There was also considerable experimentation with lemmatizing text to reduce features and consolidate the weights of words. The models with lemmatizing performed worse than models without lemmatizing. So the next step was to identify if there were further features in the text to capture so the text was tokenized. Within the tokenizing search n_grams were evaluated from 1-3 words and the best n_grams were Many variations of models were run for these different iterations of text extraction through grid searching, and in the end sentiment analyis without any other text features performed best.

Within the tested neural networks RNN was used as a preliminary model, but had problems with overfitting. LSTM provided higher accuracy scores with less overfitting.

**Models: (Accuracy Score)**
*Lemmatize vs non-lemmatize*
TFIDF w/ Multinomial Bayes: 52.4%
CV w/ Multinomial Bayes: 44.2%

*Tokenize text and sentiment analysis*
TFIDF w/ Multinomial Bayes: 55.14%
TFIDF w/ RNN: 48.36%

*Only sentiment analysis*
RNN: 64.57%
LSTM: 77.02%


###  Regression Modeling using text data

In order to properly analyze the text, multiple approaches were used. Two different types of sentiment analysis were incorporated, Vader and TextBlob. Ultimately, the Vader sentiment analysis was more correlative to the direction of the price so it was used in concert with the movement in the market measured in percentage.

Text was left as raw as possible for the regression models to create a baseline of understanding to see if further and more substantial analysis was merited. This means that the data used for the regression models were not lemmatized, nor were key words and stop words utilized to alter the outcome.

Overall, 8 different regression models were tested using a basic pipeline.

Linear Regression
Gradient Boost
KNeighbors
Ridge
Extra Trees
Random Forest
Lasso
Decision Tree
Based on R2 scores, the top three performing models were selected and put through a gridsearch to optimize their potential.

Random Forest - 0.32MSE, 0.10MAE
Extra Trees - 0.23MSE, 0.36MAE
Decision Tree - 0.32MSE, 0.45MAE
Consistent with the other modeling techniques used, the Random Forest regressor performed well enough to justify further modeling and analysis.


### Classification and Regression Modeling using no text data

**Classification Models: (Accuracy Score)**
- Multinomial Bayes: 0.55
- FFNN: 0.80
- Recurrent Neural Network (RNN): 0.65
- LSTM: 0.81 
- Logistic Regression: 0.44 
- KNN: 0.77
- Decision Tree: 0.78 
- Bagging Classifier: 0.79
- Random Forest: 0.80 
- Gradient Boosting: 0.81
- XGB Classifier: 0.80
- SVC: 0.80

**Regression Models: (MSE)**
- Gradient Boosting: 6.30E-05
- Random Forest Regressor: 6.73E-05
- Bagging Regressor: 6.52E-05
- LSTM: 7.61E-05
- FFNN: 7.69E-05
- Decision Tree Regressor: 8.06E-05
- Linear Regression: 8.13E-05
- RNN: 1.20E-04
- SVR: 2.19E-04


## Results

Random Forest Classifier

Feature:     Importance

- Open_pct_l1:        0.031
- close_pct_l1:       0.479
- Volume_diff_l1:     0.223
- is_holiday_1:       0.024
- day_of_week_1:      0.004
- day_of_week_2:      0.004
- day_of_week_3:      0.007
- day_of_week_4:      0.009
- day_of_week_5:      0.005
- day_of_week_6:      0.215


*Gradient Boosting Regressor*

Feature:     Importance

- Open_pct_l1:        0.017
- close_pct_l1:       0.973
- Volume_diff_l1:     0.008
- is_holiday_1:       0.000
- day_of_week_1:      0.001
- day_of_week_2:      0.000
- day_of_week_3:      0.001
- day_of_week_4:      0.000
- day_of_week_5:      0.000
- day_of_week_6:      0.000


## Conclusions
Can sentiment analysis on business articles coupled with other NLP techniques predict S&P 500 price data  with greater than 50% accuracy?
YES! The models incorporating tokenized text (55.13%) and only sentiment (77.01%) beat that 50% bar. But the best models in prediction did not incorporate the news. The bar of 50% appears to be low after identifying ways to identify pricing trends using purely data from previous days. One possible theory for the model to not perform as well with sentiment of text is that it created more noise than aid. The correlating factors between sentiment of news and price direction were not particularly strong.

Hyrum to discuss regression conclusions
**Best Regression Model using Sentiment Analysis**
Random Forest Regressor - 0.105MAE<br>
This Regression analysis was a stepping stone to determine vaibility of concept and to stand as a baseline for further effort. With a 10.5% mean average error, it more than exeeded expectations and further analysis is warranted.

**Best Models WITHOUT using news data**
Random Forest Classifier - 80% Accurate
Gradient Boosting Regressor - 6.03E-05

Focusing on the percent change of closing/opening prices along with volume difference is a better use of your forecasting power in predicting market movement.


### Future Recs
- Try different news sources (Bloomberg/Wall Street Journal)
- Try multiple news sources 
- Try social media posts to gauge market sentiment instead
- Try more advanced word vectorizers 
- Incorporate other features about the market such as the moving average, dividends, earnings reports etc. 
