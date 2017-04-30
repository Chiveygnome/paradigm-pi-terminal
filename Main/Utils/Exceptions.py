import exceptions

class TwitterException(exceptions.Exception):
    pass

class FileNotFoundException(exceptions.IOError):
    pass
