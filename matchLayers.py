from appscript import *
from mactypes import *
from InfraPy import *


find = app('Finder')
il = app('Adobe Illustrator')



# read the settings of the current document
docName = il.current_document.name()
doc1 = il.documents[docName]
layers = doc1.layers()
layerList = []
opacityList = []
colorList = []
filledList = []
strokedList = []
strokeList = []
fillList = []
dashList = []
# loop through layers of current document
# store a value for each layer
for layer in layers:
    layerList.append(layer.name())
    item = layer.path_items()[0]
    opacityList.append(item.opacity())
    strokedList.append(item.stroked())
    filledList.append(item.filled())
    colorList.append(item.stroke_color())
    strokeList.append(item.stroke_width())
    fillList.append(item.fill_color())
    dashList.append(item.stroke_dashes())



inFolder = "/Users/benjamingolder/Desktop/Workshops/flyers/vaults"
inPrefix = ""
outFolder = inFolder
outPrefix = "vaultwork"
paths = listFiles(inFolder, True, fileExtension=".ai")
exportPaths = editFileExt('.ai', '.png', editFilePrefix( inFolder+'/'+inPrefix , outFolder+'/'+outPrefix , paths ) )

for i in range(len(paths)): # This is an appropriate place to limit the number of files
    path = paths[i]
    export = exportPaths[i]
    f = File(path)


    il.open(f)
    # switches the doc ref to the newly opened document
    doc = il.current_document()
    for j in range(len(layerList)):
        layerName = layerList[j]
        opacity = opacityList[j]
        color = colorList[j]
        stroke = strokeList[j]
        fill = fillList[j]
        dashes = dashList[j]
        stroked = strokedList[j]
        filled = filledList[j]
        layer = doc.layers[layerName]
        try:
            layer.opacity.set(opacity)
            for item in layer.path_items():
                item.stroked.set(stroked)
                item.filled.set(filled)
                if stroked:
                    item.stroke_color.set(color)
                    item.stroke_width.set(stroke)
                    item.stroke_dashes.set(dashes)
                if filled:
                    item.fill_color.set(fill)
            layer.move(to=doc.end)
        except:
            pass

    doc.save(in_=export, as_=k.PNG24)
    doc.close(saving=k.no)
