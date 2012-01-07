import os
import csv
import cPickle as pickle

def loadRows(filePath):
    reader = csv.reader( open(filePath, 'rb'))
    rows = [r for r in reader]
    return rows

def unpickle(path):
    f = open(path, 'rb')
    data = pickle.load(f)
    f.close()
    return data

def getWaterData(row):
    sid = row[0]
    dbFolder = '/Users/benjamin/projects/amigos/db'
    watermask = '%swaterdata'
    datapath = os.path.join( dbFolder, watermask % sid )
    try:
        data = unpickle(datapath)
        return data
    except:
        print 'unable to unpickle', datapath


def addColsToHeader( header, dictionary ):
    for k in dictionary:
        header.append(k)
    return header

def addDataToRows( rows, datas, header ):
    out = []
    for i, r in enumerate(rows):
        d = datas[i]
        out.append( addDataToRow( r, d, header ))
    return out

def addDataToRow( row, data, header, joinString='/' ):
    lenDiff = len(header) - len(row)
    cols = header[-(lenDiff):]
    for k in cols:
        if k in data:
            cell = data[k]
            if type(cell) in (list, tuple):
                cell = joinString.join(cell)
            row.append(cell)
        else:
            row.append('')
    return row

def formatRow( row ):
    return '%s\n' % ','.join(['"%s"' % c for c in row])


def writeCSV( header, rows, filePath ):
    f = open(filePath, 'w')
    f.write( formatRow( header ))
    for row in rows:
        f.write( formatRow( row) )
    f.close()

if __name__=='__main__':
    folder = '/Users/benjamin/projects/amigos/merge'
    csvFile = os.path.join(folder, 'merge.csv')
    outFile = os.path.join(folder, 'moremerge.csv')
    allrows = loadRows( csvFile )
    rows = allrows[1:]
    datas = [getWaterData(r) for r in rows]
    header = addColsToHeader( allrows[0], datas[2] )
    print header
    newrows = addDataToRows( rows, datas, header)
    print newrows[3]
    print newrows[6]
    writeCSV( header, newrows, csvFile)
    print 'done'












