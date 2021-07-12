"""Reddit Praw

This script...
"""

import praw
import pandas as pd
from itertools import cycle
import time
import sys

class redditpraw:
    pass

reddit = praw.Reddit('bot1', config_interpolation="basic")

#All possible MBTI Types
MTBTI_TYPES = ["ISTJ", "ISTP", "ISFJ", "ISFP", "INFJ", "INFP", "INTJ", "INTP", 
            "ESTP", "ESTJ", "ESFP", "ESFJ", "ENFP", "ENFJ", "ENTP", "ENTJ"]
COLS = ["redditor", "type", "text"]

def get_redditors_from_subreddit(subreddit_group):
    """Goes through comments of a subreddit and adds the author of 
    the comment to a set of redditors. This is a workaround until we 
    find or use an API that gets all redditors from a subreddit. 

    Parameters
    ----------
    subreddit_group : str
        subreddit to search.

    Returns
    -------
    users
        a set of redditors stored in the variable users.
    """

    users = set()
    for comment in reddit.subreddit(subreddit_group).comments(limit=100):
        author = comment.author
        users.add(str(author))
    return users

def get_user_texts(user):
    """Goes through the user's submissions and extracts their text into
    a list of texts.

    Parameters
    ----------
    user : str
        a user or redditor.

    Returns
    -------
    texts : list
        a list of the user's texts.
    """

    texts = []
    for submission in reddit.redditor(user).submissions.new(limit=10):
        if submission.selftext:
            texts.append(submission.selftext)
    
    return texts

def generate_data(reddit_data):
    """Generate a data frame with the given data.

    Parameters
    ----------
    reddit_data : list
        The preprocessed data. It is a list of tuples.  
    """

    if reddit_data:
        reddit_df = pd.DataFrame(reddit_data, columns=COLS)
        return reddit_df

def generate_data_file(reddit_df, file_name):
    """Generate a data file and save that 
    object as a csv with the name of file_name.

    Parameters
    ----------
    file_name : str
        The name of the file. 
    """

    reddit_df.to_csv('.\data\{}.csv'.format(file_name), index = False, header=True)

def get_user_type(user):
    """Given a user or redditor retruns the user's personality 
    type based off of what the user used as their flair. Since 
    a user may have updated their flair over time this method
    also ensures that it returns only a flair that is in the list of
    MTBTI types. 

    Parameters
    ----------
    user : str
        a user or redditor.

    Returns
    -------
    users
        a user's personality type.
    """

    type = ""
    flairs = []
    for submission in reddit.redditor(user).submissions.new(limit=100):
        if submission.author_flair_text in MTBTI_TYPES:
            flairs.append(submission.author_flair_text)
    if flairs:
        type = max(set(flairs), key=flairs.count)
    
    return type

def process_data_to_file(subreddit_group, file_name):
    """This method acts to pull everything together and generate 
    a data file. 

    Parameters
    ----------
    subreddit_group : str
        a subreddit you want to search.
    file_name : str
        the name of the file you want to save your data under.
    """

    users = get_redditors_from_subreddit(subreddit_group)
    data = []
    for user in users:
        type = get_user_type(user)
        texts = get_user_texts(user)
            
        if texts:
            data.append(list(zip(cycle([user]), cycle([type]), texts)))

    reddit_data = [item for sublist in data for item in sublist]
    reddit_df = generate_data(reddit_data)
    generate_data_file(reddit_df, file_name)

def process_data_to_df(subreddit_group):
    """This method acts to pull everything together and generate 
    a data frame. 

    Parameters
    ----------
    subreddit_group : str
        a subreddit you want to search.
    """

    users = get_redditors_from_subreddit(subreddit_group)
    data = []
    for user in users:
        type = get_user_type(user)
        texts = get_user_texts(user)
            
        if texts:
            data.append(list(zip(cycle([user]), cycle([type]), texts)))

    reddit_data = [item for sublist in data for item in sublist]
    reddit_df = generate_data(reddit_data)
    return reddit_df

if (__name__ == '__main__'):
    time = time.time()

    print("""
    #########################################################################################
    #########################################################################################
    Usage: This script acts to pull everything together and generate 
    a data file.
    Expalain....
    Parameters:
        subreddit_group (string): name of subreddit group to search.
        file_name (string): name of of the file you want to save your data under.
        
    Examples:
        python3 redditpraw.py 'ENFJ' 'test_file'
        python3 redditpraw.py d 'test_file'
        python3 redditpraw.py
    #########################################################################################
    #########################################################################################

        """)

    # Defaults:
    subreddit_group = "ENFJ"
    file_name = "personality_data_{}".format(time)

    # Command line inputs
    if len(sys.argv) > 1:
        if sys.argv[1] != 'd':
            subreddit_group = sys.argv[1]
        if sys.argv[2] != 'd':
            file_name = sys.argv[2]

    print("Generating data...")
    process_data_to_file(subreddit_group, file_name)