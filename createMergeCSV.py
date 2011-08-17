import os
import macpath

def rowsToXLS( filename, rows ):
    f = open( filename, 'w')
    for row in rows:
        f.write( ','.join(row))
        f.write('\n')
    f.close()
    print 'rows written to %s' % filename



if __name__=='__main__':
    imageFolder = '/Users/benjamin/projects/amigos/tifs'
    outputFolder = '/Users/benjamin/projects/amigos/merge'
    outfile = os.path.join(outputFolder, 'merge.csv')

    allContents = os.listdir(imageFolder)
    sids = [f[-7:-4] for f in allContents]
    layers = [f[:-8] for f in allContents]

    sids = set(sids)
    layers = set(layers)

    rows = []
    header = ['@%s' % lay for lay in layers]
    rows.append(header)

    for sid in sids:
        row = []
        for layer in layers:
            baseName = '%s-%s.tif' % (layer, sid)
            folder = imageFolder.replace('/',':')
            path = '"%s"' %  macpath.normpath(macpath.join('Macintosh HD',folder,
                baseName))[1:]
            row.append(path)
        rows.append( row)

    rowsToXLS( outfile, rows)







