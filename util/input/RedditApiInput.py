import praw
import sys, os
class RedditApiInput:
    redditUrl = "https://www.reddit.com"
    def __init__(self):
        self.reddit = praw.Reddit("test")
        
    def get(self,subreddit):
        return self.reddit.subreddit(subreddit).hot(limit=1)

def main():
    reddit = RedditApiInput()
    for submission in reddit.get("askreddit"):
        print(submission)
if __name__ == "__main__":
    main()
