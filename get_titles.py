import praw
import pickle
from teams import teamName
from config import reddit

for team in teamName:
	print(team)
	submission_titles = []
	fh = open("subreddit_data/titles/" + team + "_titles.py", "wb")
	pickle.dump(submission_titles, fh)
	fh.close()
	fh = open("subreddit_data/ids/" + team + "_ids.py", 'rb')
	submission_ids = pickle.load(fh)
	for i in submission_ids:
		submission = reddit.submission(id = i)
		submission_titles.append(submission.title)
	fh = open("subreddit_data/titles/" + team + "_titles.py", 'wb')
	pickle.dump(submission_titles, fh)
	fh.close()