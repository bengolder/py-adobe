import os
import macpath

class ImageLayer:
    def __init__(self):
        self.ext = None
        self.name = None


def listsToCSV( filename, rows ):
    f = open( filename, 'w')
    for row in rows:
        f.write( ','.join([str(i) for i in row]))
        f.write('\n')
    f.close()
    print 'rows written to %s' % filename

def harvestFromFolder( folder, idInterval, layerInterval ):
    allContents = os.listdir( folder )
    rawIds = [f[idInterval[0]:idInterval[1]] for f in allContents]
    rawLayers = [f[layerInterval[0]:layerInterval[1]] for f in allContents]
    ids = set( rawIds )
    layers = set( rawLayers )
    return ids, layers

def renames( folder ):
    files = os.listdir(folder)
    inPaths = [os.path.join(folder, f) for f in files]
    outPaths = [s.replace('_shadow','') for s in inPaths]
    for i, p in enumerate(inPaths):
        os.rename(p, outPaths[i])

def getFileBits(folder, fileName, layerInterval, idInterval):
    layer = fileName[layerInterval[0]:layerInterval[1]]
    sid = int(fileName[idInterval[0]:idInterval[1]])
    morePath = os.path.join(folder, fileName)
    path = morePath.replace('/',':')
    fullPath = '"Macintosh HD%s"' % path
    return sid, layer, fullPath


def harvestRowsFromFolders( folderList, idInterval, layerInterval ):
    rows = {}
    layers = set()
    for folder in folderList:
        contents = os.listdir(folder)
        contents.remove('.DS_Store')
        for f in contents:
            sid, layer, path = getFileBits(folder, f, layerInterval, idInterval)
            if layer not in layers:
                layers.add(layer)
            if sid not in rows:
                rows[sid] = {}
            rows[sid][layer] = path
    return rows, layers

def joinRows( rows1, rows2 ):
    for sid in rows1:
        if sid in rows2:
            rows1[sid].update(rows2[sid])
        else:
            rows1[sid] = rows2[sid]
    return rows1

def buildLists( rows, layers ):
    header = ['sid']
    layerList = list(layers)
    header.extend(['@%s' % n for n in layerList])
    out = [header]
    for sid in rows:
        newRow = [sid]
        for column in layerList:
            if column in rows[sid]:
                newRow.append(rows[sid][column])
            else:
                newRow.append('')
        out.append(newRow)
    return out





if __name__=='__main__':

    imageFolder = '/Users/benjamin/projects/amigos/tifs'
    watershedFolder = '/Users/benjamin/projects/amigos/newAI'

    outputFolder = '/Users/benjamin/projects/amigos/merge'
    outfile = os.path.join(outputFolder, 'merge.csv')

    imageRows, layers = harvestRowsFromFolders( [imageFolder], (-7,-4), (None,-8) )
    watershedRows, nlayers = harvestRowsFromFolders( [watershedFolder], (None, -14), (-13,-3) )
    allRows = joinRows( imageRows, watershedRows )
    layers |= nlayers

    rowLists = buildLists( allRows, layers )

    listsToCSV( outfile, rowLists)







