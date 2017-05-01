import threading
from Exceptions import twitterException
import twitter

class _TwitterCallAbstract(threading.Thread):
    
    self._message = ""
    self._api = None

    def __init__(self, cKey, cSecret, aKey, aSecret, message, *args, **kwargs):
        super(_TwitterCallAbstract, self).__init(args, kwargs)
        self._message = message
        self._api = twitter.Api(consumer_key=cKey, consumer_secret=cSecret,
                                access_token_key=aKey, access_token_secret=aSecret)


    def _run_(self):
        raise NotImplementedError("Reimplement this when subclassing")

    def run(self):
        self._startup_()
        self._run_()

    def _startup_(self):
        pass
    
class TwitterPost(_TwitterCallAbstract):
    pass
    