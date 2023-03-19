import praw
import sys
class RedditApiInput:
    redditUrl = "https://www.reddit.com"
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.reddit = praw.Reddit(
            client_id = self.client_id,
            client_secret = self.client_secret,
            user_agent = "AutoTube"
        )
        
    def get(self,subreddit):
        return self.reddit.subreddit(subreddit).hot(limit=10)

def main():
    reddit = RedditApiInput(client_id=sys.argv[1], client_secret=sys.argv[2])
    for submission in reddit.get("askreddit"):
        print(submission)
if __name__ == "__main__":
    main()
