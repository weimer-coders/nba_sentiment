from textblob import TextBlob
import pickle
import csv
from teams import teamName

csvfile = open("subreddit_data/sentiment_results.csv", "w")
writer = csv.writer(csvfile)
writer.writerow(["Team", "Total Comments", "Positive", "Percent Positive", "Negative", "Negative Percentage"])


for team in teamName:
	print(team)
	pos_count = 0
	neg_count = 0

	f = open("subreddit_data/comments/" + team + "_comments.py", "rb")
	fp = pickle.load(f)

	for comment in fp:
		comments_blob = TextBlob(comment)
		comment_sentiment = comments_blob.sentiment.polarity

		if comment_sentiment > 0.2:
			pos_count += 1
		elif comment_sentiment < -0.2:
			neg_count += 1

	total_comments = pos_count + neg_count
	pos_percentage = round((pos_count/total_comments) * 100)
	neg_percentage = round((neg_count/total_comments) * 100)

	writer.writerow([team, total_comments, pos_count, pos_percentage, neg_count, neg_percentage])

	f.close()

csvfile.close()