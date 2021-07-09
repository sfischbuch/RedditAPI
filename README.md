# RedditAPI
Learning the Reddit API via a project using NLP and personality types.

# Setup
1. Go to reddit.com/prefs/apps and create an app and obtain the client_id and client_secret. Use http://localhost:8080 as 
your redirect uri or your user context such as a web site.
2. To protect your credentials create a praw.ini file to place them in. Place this in the working directory. This is not the best 
way to authenticate but it will do for now. 
3. Configure and create a Reddit intances with praw.Reddit('site name in .ini file').

# Tips
1. Make sure if you are using a virtual env that you tell your IDE to use the path to python.exe that is in the ./env directory of your virtual env.  

# Reddit terms and concepts
**A subreddit** - is a specific online community, and the posts associated with it, on the social media website Reddit. Subreddits are 
dedicated to a particular topic that people write about, and they're denoted by /r/, followed by the subreddit's name, e.g., /r/gaming.

**Submission** -

**Redditor** - a registered user of the website Reddit.

**user_agent** - The user_agent field is how we uniquely identify our script. See https://github.com/reddit-archive/reddit/wiki/API

**Reddit Instance** - Reddit() Config for praw and creating the Reddit instance. Read-only does not require userneam and password but only allows 
you access to public information.

# Resources 
**PRAW Docs:** https://praw.readthedocs.io/en/v7.3.0/
