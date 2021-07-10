import praw
import pandas as pd
from itertools import cycle

reddit = praw.Reddit('bot1', config_interpolation="basic")

redditors = ["an-average-white-guy"]

type = ["INTJ"]
texts = []

for submission in reddit.redditor(redditors[0]).submissions.new(limit=10):
    texts.append(submission.selftext)
    #print(submission.selftext)

data = list(zip(cycle(redditors), cycle(type), texts))
reddit_df = pd.DataFrame(data, columns='redditor, type, text'.split())
reddit_df.to_csv(r'.\data\personality_data.csv', index = False, header=True)
