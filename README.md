# NLP Capstone Project: Airline Sentiment Classification

## Dataset Description from Kaggle:
1. The Kaggle Dataset contains tweets and categories for `14,640k airline related tweets`,
classified into one of `3 sentiment categories:` **(positive, negative, neutral)**.<br>
2. Tweets were scraped from February of 2015 and contributors were asked to classify tweets into positive, negative, and neutral categories.<br>
3. They were also asked to categorize the negative category tweets into negative reason topics (such as “late flight” or “rude service”).

`Link to Dataset: `   https://www.kaggle.com/crowdflower/twitter-airline-sentiment/data

## Problem Statement

This data science project aims to help airline companies determine customer satisfaction,
through feedback from twitter data.<br>

## Project Goal 

Use the airline sentiment dataset from kaggle and pulled customer feedback from twitter,
to evaluate how well Natural Language Processing and machine learning modelling techniques, can achieve the following two tasks.<br>
1. Predictive text sentiment classification.
2. Topic inference from unknown text, through unsupervised learning models, such as LDA.<br>
   (This portion of the project is still in progress).

## Challenges
1. Text language can be very challenging to classify due to the ambiguity and subjectivity in the data.<br>
2. This is specially true for twitter text data, since users use a lot of figurative language, emojis, abbreviations and so on.
3. There is also not much classified airline sentiment data available, so training models with a substantial amount of data can be difficult. This may affect the models performance in generalizing well to unseen data. 
4. Then there is the issue of class imbalance in the training dataset. This dataset's negative class is highly imbalanced. For this capstone project I used an unbalanced dataset, to explore and see what results could be achieved. 
5. The next step of this project will be to explore "dealing with class imbalance", which is a very common problem in real world datasets.

### What have I done so far?

1. <b>Exploration and Analysis of the data</b>:
  1. Standardized case (to lower)
  2. Removed puntuations
  3. Removed stop words
  4. Normalized data using stemming/lemmatization.
    1. Lemmatization: look for base of the word.<br>
       am, are, is $\Rightarrow$ be<br> 
       car, cars, car's, cars' $\Rightarrow$ car
    2. Stemming: chops off the end of words based on certain alogithms.<br>
        The most common seems to be Porter's algorithm.<br>
        sses, ies, ss, s $\Rightarrow$ ss, i, s, ''<br>
        caresses, ponies, caress, cats $\Rightarrow$ caress, poni, caress, cat
  5. Encoded emojis separately as individual features.
    1. Extracted emojis from input text.
    2. Unclumped emojis, since users group them together.<br>
    `NOTE`: Can continue to further explore using group of emojis as features.
    3. Created a dictionary of emojis and codes for all the emojis found in the dataset.<br>
    `NOTE`: Can continue to further explore expanding the emoji features supported.<br>
  6. Looked at effects of dimensionality reduction by separately
     <br>analyzing 'clean_text', 'adding stopwords', 'adding stemming', 'lemmatizing'.
  7. Explored characteristics of different n-gram features, using CounVectorizer.<br>
     Looked at the classifier words:
    1. What are the top words for each category, with the different processed texts? 
      1. Made a wordcloud for each category.
      2. Made bar charts of top 50 words for each category.<br>
     `NOTE`: Can further explore this by using TfidfVectorizer to see the differences.<br><br>
2. <b>Modeling</b>
  1. What effects do emojis have on model predictions?
    1. Created model pipelines for data with and without `emoji encoding`.<br>
  2. What effects do different levels of text processing, which is a way of doing<br>
     feature dimensionality reduction, have on model predictions?
    1. Created model pipelines for different levels of text processing.
  3. Used `CountVectorizer` to transform the text data.<br>
     `NOTE`: Can continue to further explore using TfidfVectorizer,<br>
     to see which performs better as a preprocessing step.
  4. Tested out two classifiers: `NaiveBayes` and `Logistic Regression`, using cross validation.
    1. Why did I choose these two classifiers?<br>
       From my understanding both have differnt learning mechanisms:<br>
       <b>Naive Bayes</b>:<br>
       Naive Bayes models the joint distribution (X,Y) and then predicting the<br>
       probability P(y| x) where X is the set of inputs features and Y is the output labels.<br>
       Basically it uses the training data to estimate P(X|Y) and P(Y). It then uses<br>
       these together with bayes rule P(Y|X)=P(X|Y)*P(Y)/P(X), to predict a Y for a<br>
       new X.<br>
       <b>Logistic Regression</b>:<br>
       Logistic regression directly models the P(y|x) from learning the input to output mapping,<br>
       by minimizing the prediction.
  5. Ran a gridsearch to find the best model for each classifier, by tunning hyper parameters.
    1. Did grid searching improve the results?
  6. Model evaluation.
    1. Evaluated the classifiers by analyzing `accuracy`, `precision` and `recall` metrics,<br>
    using confusion matrix and classification report.
    1. What effects did different dimensionality reduction and preprocessing<br>
       methods have on the results?<br><br>
3. <b>LDA (Latent Dirichlet allocation) topic modeling.</b>
  1. Given a corpus of text, what topics can be extracted from it?
    1. Created LDA models using Gensim and Sklearn to see what topics<br>
       were learned from the text. (used text processed using stopwords and lemma)
    2. Visualized topics generated from the training data.
  2. Pulled tweets with hashtags of major US Airlines and trained LDA model<br>
     to see what topics were learned from the data.
     
     (NOTE: LDA topic modeling is work in progress...)
     
### Next Step:     Dealing with class imbalance

1.  Resample the most frequent class to have a similar size as the other classes.
2.  Tune the penalty hyperparameter of Logistic Regression.
3.  Evaluate other algorithms which deal well with imbalanced datasets.
    1. Decision trees may perform well on imbalanced datasets. The splitting rules that look at the class 
       variable used in the creation of the trees, can force both classes to be addressed.