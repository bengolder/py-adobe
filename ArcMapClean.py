from appscript import *

il = app('Adobe Illustrator')
doc = il.current_document()
lyrs = doc.layers()


# for each layer
for lyr in lyrs:
    if lyr.name() == 'Layers':
        layers = lyr.layers()
        for layer in layers:
            print layer.name()
            print layer.group_items()
            print len(layer.group_items())
            grp = layer.group_items()[0]
            print grp.clipped()
            print help(grp)


    # get the groups in the layer
    # for each group



