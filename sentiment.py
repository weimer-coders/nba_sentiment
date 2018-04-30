from textblob import TextBlob
import pickle
from teams import teamName

# Two empty lists, one for positive words and one of negative words.
pos_list = []
neg_list = []

for team in teamName:
	print(team)
	fh = open("subreddit_data/comments/" + team + "_comments.py", "rb")
	submission_comments = pickle.load(fh)
	for comment in submission_comments:
		comments_blob = TextBlob(comment)
		comment_sentiment = comments_blob.sentiment.polarity
		# Prints out the sentiment scores for each word in the data list.
		# print(comment_sentiment)

		# If the sentiment analyzer gives a compound score percentage higher than 0.2, append it to the positive list. If less than -0.2, append to negative list. This will give you less false postives and false positives, but will significantly reduce the size of the results.
		if comment_sentiment > 0.2:
			pos_list.append(comment)

		elif comment_sentiment < -0.2:
			neg_list.append(comment)

	# Write lists to files. 
	with open("subreddit_data/sentiment_comments/" + team + "_pos_comment_list.txt", "w", encoding="utf-8", errors="ignore") as f_pos:
		for comment in pos_list:
			f_pos.write(comment + "\n")

	with open("subreddit_data/sentiment_comments/" + team + "_neg_comment_list.txt", "w", encoding="utf-8", errors="ignore") as f_neg:
		for comment in neg_list:
			f_neg.write(comment + "\n")

	fh.close()