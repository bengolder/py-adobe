from appscript import *
from mactypes import *
from InfraPy import *

il = app('Adobe Illustrator')


paths = listFiles("/LocalCodeFullBatch/DNABarsAI", True, fileExtension=".ai")
exportPaths = editFilePrefix("/LocalCodeFullBatch/DNABarsAI/DNABarsAI",
                        "/LocalCodeFullBatch/DNABarsRefined/DNABarsRefined", paths)

for i in range(len(paths)):
    path = paths[i]
    export = exportPaths[i]
    f = File(path)


    il.open(f)
    # switches the doc ref to the newly opened document
    doc = il.current_document()
    items = doc.page_items.get()
    for item in items:
        color = item.stroke_color.get()
        neg = item.filled.get()
        item.fill_color.set(color)
        item.stroked.set(neg)




    doc.save(in_=export, as_=k.Illustrator)
    doc.close(saving=k.no)




