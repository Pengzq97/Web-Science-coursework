
"""
usable version to crawl tweets from hash tag
"""

# # # # TWITTER ACCOUNT CONFIG # # # #

CONSUMER_KEY=""
CONSUMER_SECRET=""
ACCESS_TOKEN="-"
ACCESS_TOKEN_SECRET=""

# YouTube Video: https://www.youtube.com/watch?v=wlnx-7cm4Gg
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import emoji


# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """

    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """

    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        if status == 420:
            # Returning False on_data method in case rate limit occurs.
            print(status)
            return False



if __name__ == '__main__':
    # Authenticate using config.py and connect to Twitter Streaming API.
   # happy=["#happy","#glad","#love","#cheer", "#enjoy", "#joy","#happiness","#smile", "#like",emoji.emojize('')]
    total = ["#happy", "#glad", "#love", "#cheer", "#enjoy", "#joy", "#happiness", "#smile",
             emoji.emojize(':laughing:', use_aliases=True),
             "#comfort", "#confident", "#relax", "#content", "#satisfied", emoji.emojize(':relaxed:', use_aliases=True),
             "#exciting", "#excited", '#amazing', '#amazed', emoji.emojize(':exclamation:', use_aliases=True),
             emoji.emojize(':punch:', use_aliases=True),
             "#sad", "#tense", "#frustration", "#distressed", emoji.emojize(':cry:', use_aliases=True),
             "#afraid", "#alarm", "#anxiety", "#concerned", "#disgust",'#horrible',"#panic",emoji.emojize(':fearful:', use_aliases=True),
             "#angry", "#annoyed", "#bear", "#mood", emoji.emojize(':triumph:', use_aliases=True)]

    fetched_tweets_filename = "7_version.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, total)
