from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


# Consumer key, consumer secret, access token, access secret
ckey="KBhEbR7mtJFiAHbZg9hEw0Udk"
csecret="oTXaRZJtJe2gs9v0sT0X1d641lJukcvu8HWDCHoxAFBTNz5kgD"
atoken="971808625122533378-E5G9EvNrIdyCjDEGGOV4qHO5J7Ca1ZY"
asecret="j8oyDotC6LZcmW9XUoXs3qAwhqIbi2IxjACHuQuDkgrbW"


class MyListener(StreamListener):

    def on_data(self, data):
        print(data)
        return (True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, MyListener())
twitterStream.filter(track=["BuenJueves"])
