# nba_sentiment 🏀

nba_sentiment is a sentiment analysis project written in python that inspects every comment posted on an [NBA subreddit](https://www.reddit.com/r/nba/) from October 16, 2017 through March 31, 2018. At the end you can see which NBA subreddits were the most positive or negative. Made by [Mary-Lou Watkinson](https://twitter.com/Mary_Lou_W) and [Ryan Serpico](https://twitter.com/zuckerco).

## Requirements

All the requirements you will need for the project are stored in the [requirements.txt file](https://github.com/weimer-coders/nba_sentiment/blob/master/requirements.txt). 

Python libraries used for the project include:
* [TextBlob](https://textblob.readthedocs.io/en/dev/): A textual data analysis library. This does the sentiment analysis for nba_sentiment.
* [PRAW](https://praw.readthedocs.io/en/latest/): A python wrapper for the Reddit API.

## Setting up PRAW

1. [Follow PRAW's documentation to get a client_id, client_secret and user_agent for your reddit instance.](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html)
2. Create a new file and name it `config.py`.
3. In `config.py`, paste in the following code and replace PLACEHOLDER with the keys that you got by following step 1:
```python
reddit = praw.Reddit(client_id='PLACEHOLDER',
                     client_secret='PLACEHOLDER',
                     user_agent='PLACEHOLDER')
```

## Get Submission IDs

In order to get comments from every NBA subreddit, you need to get the ID of every submission posted to each subreddit. Do the following to accomplish that:

1. Rev up Terminal on your Mac and `cd` into where you downloaded nba_sentiment to.
2. In Terminal, run `python get_ids.py`.
3. It will go into each NBA team's subreddit using [this python list](https://github.com/weimer-coders/nba_sentiment/blob/master/teams.py) and will grab every submission's ID.

NOTE: Reddit is [deprecating the tool](http://praw.readthedocs.io/en/latest/package_info/change_log.html?highlight=deprecated) that allowed us to collect the IDs for posts within a specific date range. By the time you read this, you may not be able to reproduce the method that we used. Sorry.

## Get Submissions/Comments

Once you get the IDs for every submission on every team's subreddit, you can get every comment. 

1. Open Terminal back up and `cd` into where you downloaded nba_sentiment to.
2. In Terminal, run `python get_comments.py` to get your comments.
3. Again, it will go into each NBA team's subreddit using [this python list](https://github.com/weimer-coders/nba_sentiment/blob/master/teams.py) and will grab comments from every submission.

## Perform Sentiment Analysis with TextBlob

OK. You have your commments. Cool. Know you can perform sentiment analysis on them so that you can see which subreddits were being more negative or positive. 

1. In Terminal, navigate back into nba_sentiment.
2. Run `python sentiment.py`.
3. This python script looks at the comments you grabbed in the previous step and uses TextBlob to determine if a comment is either postive or negative. It increases what is considered a neutral comment in order to eliminate any false postives or negatives. Depending how it is labeled, each comment will go into a positive comment text file or a negative comment text file for each team. 

## Store Sentiment Analysis Results in a CSV file.

Alrighty. If you're still with us, the payoff is near. 

Having two sentiment text files for each team is great, but you'll want to get some basic statistical conclusions from them.

1. Navigate to nba_sentiment in terminal, one last time.
2. Run `python count_comments.py`
3. Open `sentiment_results.csv` to see the results.

Just like the sentiment analysis in the previous section boosted the buffer for neutral comments to get rid of any false positives or negatives, this one does too. It does some elementary school math to calculate the total comments in each subreddit, the number of positive and negative comments and the percentage of total comments that are positive or negative.

## The End
That's all folks!
