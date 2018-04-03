import praw
from config import reddit
import pickle
from teams import teamName

for team in teamName:
	print(team)
	submission_comments = []
	fh = open("subreddit_data/comments/" + team + "_comments.py", "wb")
	pickle.dump(submission_comments, fh)
	fh.close()
	fh = open("subreddit_data/ids/" + team + "_ids.py", 'rb')
	submission_ids = pickle.load(fh)
	for i in submission_ids:
		submission = reddit.submission(id = i)
		submission.comments.replace_more(limit=None)
		for comment in submission.comments.list():
			submission_comments.append(comment.body)
	fh = open("subreddit_data/comments/" + team + "_comments.py", 'wb')
	pickle.dump(submission_comments, fh)
	fh.close()
