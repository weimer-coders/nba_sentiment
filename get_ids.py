import praw
import pickle
from teams import teamName
from config import reddit

for team in teamName:
	submission_ids = []
	fh = open(team + "_ids.py", "wb")
	pickle.dump(submission_ids, fh)
	fh.close()
	subreddit = reddit.subreddit(team)
	for submission in subreddit.submissions(1508284800, 1522454400):
		submission_ids.append(submission.id)
	fh = open(team + "_ids.py", 'wb')
	pickle.dump(submission_ids, fh)
	fh.close()