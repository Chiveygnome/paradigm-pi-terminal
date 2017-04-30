import threading
from Exceptions import twitterException
import twitter

class _TwitterCallAbstract(threading.Thread):
    
    def _run_(self):
        raise NotImplementedError("Reimplement this when subclassing")

    def run(self):
        self._startup_()
        self._run_()

    def _startup_(self):
        pass
    
