# RedditAPI
An AI application that determines your Myers-Briggs Type Indicator.

# Setup
1. Go to reddit.com/prefs/apps and create an app and obtain the client_id and client_secret. Use http://localhost:8080 as 
your redirect uri or your user context such as a web site.
2. To protect your credentials create a praw.ini file to place them in. Place this in the working directory. This is not the best 
way to authenticate but it will do for now. 
3. Configure and create a Reddit intances with praw.Reddit('site name in .ini file').

# Resources 
**PRAW Docs:** https://praw.readthedocs.io/en/v7.3.0/
