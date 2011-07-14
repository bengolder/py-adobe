import xlrd
import appscript
import mactypes
import InfraPy

def addLayerToDoc(doc, layer_name=None, layer_color=None, at=None):
    layer = doc.make(new=k.layer, with_properties={k.name:self.layer_names[i], k.color:self.colors[i]}, at=doc.layers.end)


class CMYKcolor(object):
    def __init__(self, C=0.0, M=0.0, Y=0.0, K=0.0):
        self.C = C
        self.M = M
        self.Y = Y
        self.K = K
    def paint(self, other):




class NormBar(object):

    def __init__(self, vals, colors, layer_names = None, width = 1.0, height = 0.5, position=0.0):
        if len(vals) != len(colors):
            return "Error: value and color lists are different lengths."
        if layer_names != None and (len(layer_names) != len(vals)) or (len(layer_names) != len(colors)):
            return "Error: number of layer names must match the number of values and colors."
        self.vals = vals
        self.colors = colors
        self.layer_names = layer_names
        self.width = width
        self.height = height
        self.position = position
        return self

    def make(self, doc):

        if layer_names != None:

            for i in range(len(layer_names)):
                layer = doc.make(new=k.layer, with_properties={k.name:self.layer_names[i], k.color:self.colors[i]}, at=doc.layers.end)
                doc.make(new=k.rectangle, with_properties={k.color:self.colors[i], at=layer)






