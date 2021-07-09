import praw

reddit = praw.Reddit('bot1', config_interpolation="basic")

subreddit = reddit.subreddit('ENFP')

for submission in subreddit.hot(limit=10):
    print(submission.url)