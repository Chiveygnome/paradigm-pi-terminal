import threading
import twitter
from Exceptions import twitterException

class _TwitterCallAbstract(threading.Thread):
    
    self._message = ""
    self._api = None
    self._logger = None
    def __init__(self, cKey, cSecret, aKey, aSecret, message, logger, *args, **kwargs):
        super(_TwitterCallAbstract, self).__init(args, kwargs)
        self.logger = logger
        self._message = message
        self._api = twitter.Api(consumer_key=cKey, consumer_secret=cSecret,
                                access_token_key=aKey, access_token_secret=aSecret)


    def _run_(self):
        raise NotImplementedError("Reimplement this when subclassing")

    def run(self):
        self._startup_()
        self._run_()

    # Optional function for any non run loop setup
    def _startup_(self):
        pass
    
class TwitterPost(_TwitterCallAbstract):
    def __init__(self, *args, **kwargs):

        super(TwitterPost, self).__init__(args, kwargs)
    def _run_(self):
        try:
            self._logger.info("Sending {0}".format(self._message))
            self._api.PostUpdate(self._message)
        except BaseException as e:
            self._logger.error(e.message)
    