"""
A collection of convenience classes and functions for scripting the Adobe
Creative Suite on Mac OS X.
"""

import appscript
from mactypes import *

class App(object):
    def __init__(self, name):
        self.name = name
        self._app = appscript.app(name)

class InDesign:
    def __init__(self):
        self.name = 'Adobe InDesign CS4'
        self._app = appscript.app(self.name)



class IllustratorDoc(object):
    def __init__(self):
        pass


class IndesignDoc(object):
    def __init__(self):
        pass


class PhotoshopDoc(object):
    def __init__(self):
        pass


