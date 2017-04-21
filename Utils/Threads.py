import threading
from Exceptions import twitterException
from twitter_ads import client
from twitter_ads import error
from twitter_ads import http

class _twitterCallAbstract(threading.Thread):
    self.URL = ""
    self.endpoint = ""
    self.TOKEN = ""
    self.SECRET_TOKEN = ""
    self.KEY = ""
    self.SECRET_KEY = ""
    self.ID = ""
    self.tClient = None

    def _run_(self):
        raise NotImplementedError("Reimplement this when subclassing")

    def run(self):
        self._startup_()
        self._run_()

    def _startup_(self):
        self.tClient = client.Client(self.KEY, self.SECRET_KEY, self.TOKEN, self.SECRET_TOKEN)
        self.account = client.Account(self.ID)
    
class twitterGetCall(_twitterCallAbstract):
    
    """The constructor defines the get call"""
    def __init__(self, *args, **kwargs):
        super(_twitterCallAbstract, self).__init__(args, kwargs)
        self.endpoint = "Get"

    def _run_(self):
        resource = '0/accounts/{account_id}/features'.format(account_id=account.id)
        try:
            response = http.Request(tClient, self.endpoint, resource)
        except error.Error as e:
            raise twitterException(e.code+":  "+e.details)