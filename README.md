# Presidential Race - Sentiment Analysis

We are interested in exploring the different emotions of the supporters of different presidential candidates.
In this project, we are using the Twitter API to get some tweets from candidate supporters. Our goal is to identify wether is an association between one's emotional state and his choice of political candidate. We are also planning to extract some article links from news media outlets and examine the sentiment in those although this is a later task. We will use the data we get to work on some visualizations.

A quick summary of the files contained can be found below:

1. get_all_tweets - Contains a set of functions that are important to our project. These include extracting all tweets from a user's timeline, creating a csv of tweets and also contains a scrapper that extracts links from tweets of news outlets and puts them in a set for future data scraping. 

2. get_followers - Functions that gets all the followers of a specified user (both id and object)

3. main.py - Produces the csv files containing tweets of followers.
