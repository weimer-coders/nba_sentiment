import pickle
from textblob import TextBlob
from collections import Counter

loaded_comments = []

# Prints all subreddit comments for a team. Replace "mavericks" with whichever team you want.
fh = open("subreddit_data/comments/sixers_comments.py", "rb")
submission_comments = pickle.load(fh)
for i in submission_comments:
	loaded_comments.append(i)

comment_blob = TextBlob(''.join(loaded_comments))

counter = Counter(comment_blob.words).most_common(100)

file = open("sixers_count.py", "w")
file.write(str(counter))
file.close()