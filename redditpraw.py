import praw
import pandas as pd
from itertools import cycle

#Create Reddit instance and set configuration. 
# TODO add try except blocks here
reddit = praw.Reddit('bot1', config_interpolation="basic")

#All possible MBTI Types
MTBTI_TYPES = ["ISTJ", "ISTP", "ISFJ", "ISFP", "INFJ", "INFP", "INTJ", "INTP", 
            "ESTP", "ESTJ", "ESFP", "ESFJ", "ENFP", "ENFJ", "ENTP", "ENTJ"]
COLS = ["redditor", "type", "text"]
data = []

# for submission in reddit.redditor("adrianaie").submissions.new(limit=35):
#     if submission.author_flair_text in MTBTI_TYPES:
#         print("{} {} {} {} {} {} ".format(submission.author_flair_text,
#         submission.author,
#         submission.created_utc,
#         submission.id,
#         submission.name,
#         submission.title))
# Add unique redditors from the a particular subreddit.
users = set()
for comment in reddit.subreddit("ENFP").comments(limit=None):
     a = comment.author
     users.add(str(a))

for user in users:
    type = ""
    texts = []

    # Find the user's flair type.
    flairs = []
    for submission in reddit.redditor(user).submissions.new(limit=None):
        if submission.author_flair_text in MTBTI_TYPES:
            flairs.append(submission.author_flair_text)
    if flairs:
        type = max(set(flairs), key=flairs.count)

        for submission in reddit.redditor(user).submissions.new(limit=None):
            if submission.selftext:
                texts.append(submission.selftext)
        
        if texts:
            data.append(list(zip(cycle([user]), cycle([type]), texts)))

    del texts[:]
    del flairs[:]

reddit_data = [item for sublist in data for item in sublist]

if reddit_data:
    reddit_df = pd.DataFrame(reddit_data, columns=COLS)
    reddit_df.to_csv(r'.\data\personality_data4.csv', index = False, header=True)

# # TODO add main function and interface 
