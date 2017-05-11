import os
import sys
import threading
import Queue
from time import gmtime, strftime
from colorama import init
from Exceptions import FileNotFoundException

"""
    This module contains all file and logging operations.  
    'Yea, though I walk through the valley of death I will fear
    no evil' or threads.  You've been warned.
"""

RUNTIME_DIR = "run-time"


"""
    This class manages the configuration file.  The parser is quick and dirty 
    And is as general as possible only enforcing that a key-value pair be present
    and be separated by a '=' character.
"""
class ConfigManager():
    
    self.__cfgFile = None
    self.__valDict = {}

    def __init__(self, *args, **kwargs):
        super(ConfigManager, self).__init__(args, kwargs)
        for dir in os.walk(os.getcwd())[1]:
            if dir is RUNTIME_DIR:
                self._readConfig(os.path.join(os.getcwd(), RUNTIME_DIR))
                return
        raise FileNotFoundException("{} directory not found.  Exiting...".format(RUNTIME_DIR))
    
    def _readConfig(self, path):
        for f in os.walk(path)[2]:
            if f is "Config.cfg":
                self.__cfgFile = open(os.path.join(path,"Config.cfg"))
                for line in self.cfgFile:
                    if "=" in line:
                        pair = line.split("=")
                        self.__valDict[pair[0]] = pair[1]
                    else:
                        raise SyntaxError("Invalid key-value pair found.  Line: {}".format(line))
                return self.__valDict
        raise FileNotFoundException("Config.cfg not found.  Exiting...")

    def getValue(self, key):
        return self.__valDict.get(key)


class LogManager():

    self.__log = None
    self.__logFile = None
    self.shutdown = False
    self.__loggers = {}

    def __init__(self, *args, **kwargs):
        super(LogManager, self).__init__(args, kwargs)
        self.__log = Queue.Queue()
        init(autoreset=True)

    def _log(self, string):
        self.__log.put(string)

    def beginShutdown(self):
        self.shutdown = True

"""
    This class is a thread that logs all events passed to it to /RUNTIME_DIR/log.log.
    Caution must be taken when stopping this thread, because of the file operations.
"""
class _LogWriter(threading.Thread):
    
    self.__log = None
    self.__logFile = None
    self.shutdown = False
    
    def __init__(self, queue , *args, **kwargs):
        super(_LogWriter, self).__init__(args, kwargs)
        self.__logFile = open(os.path.join(RUNTIME_DIR,"log.log"), "a")
        self.__log = queue

    def run():
        while not self.shudown:
            while self.__log.empty():
                self.wait()
            self.__logFile.write(self.__log.get())
        self.__logFile.close()



"""
    Every class that has loggable events should have a member variable with
    a copy of this thread so as to log to a log file.
    
    Any class that calls this thread should not do so through the start function,
    however, they should call this from a given log function.
"""
class ClassLogger(threading.Thread):

    self.__manager = None
    self.__message = ""

    def __init__(self, manager, *args, **kwargs):
        super(ClassLogger, self).__init__(args, kwargs)
        self.__manager = manager

    def run(self):
        if self.__message is not "":
            self.__manager._log(self.__message)
            self.__message = ""

    def _log(self, level, scope, message, color):
        self.__message = "{0}: {1} at {2}: {3}".format(strftime("%Y-%m-%d %H:%M:%S", gmtime()), level, scope, message)
        print color + self.__message
        self.start()

    def debug(self, message):
        # last argument is white
        self._log("DEBUG",sys._getframe(1).f_code.co_name, message,"\033[37m")

    def warn(self, message):
        # last argument is yellow
        self._log("WARNING",sys._getframe(1).f_code.co_name, message, "\033[43m")

    def error(self, message):
        # last argument is red
        self._log("ERROR",sys._getframe(1).f_code.co_name, message, "\033[31m")

    def info(self, message):
        # last argument is white
        self._log("INFO",sys._getframe(1).f_code.co_name, message, "\033[37m")