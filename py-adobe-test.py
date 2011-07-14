from __init__ import *

def d(obj):
    for c in dir(d):
        if c[0] != '_':
            print c

indesign = App('Adobe InDesign CS4')
print indesign._app.__help__

