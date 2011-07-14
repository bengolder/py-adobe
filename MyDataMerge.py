import os
import xlrd
import xlwt

class Merge(object):
    def __init__(self, xls=None, folder=None, objects=None):
        self.xls = xls
        self.folder = folder
        self.objects = self._getObjs()

    def _getObjs(self):
        if self.xls:
            objects = self.xlsToObjs()
        else:
            objects = []
        return objects

    def xlsToObjs(self, path=None):
        if path:
            self.xls = path
        sht = xlrd.open_workbook(self.xls).sheet_by_index(0)
        col_names = [c.value for c in sht.row(0)]
        objs = []
        for n in range(sht.nrows - 1):
            vals = [c.value for c in sht.row(n+1)]
            objs.append(dict(zip(col_names, vals)))
        return objs

    def readXLS(self, path=None):
        self.objects = self.xlsToObjs(path)




if __name__=='__main__':
    f = '/Users/benjamingolder/Portfolio Resources/Projects/ARCH 299X/species-webmap-merge.xls'
    folder = '/Users/benjamingolder/Portfolio Resources/Projects/ARCH 299X/SpeciesPowerPointGroupSlides Folder/Links'
    m = Merge()
    m.xls = f
    m.folder = folder
    m.readXLS()
    #things = os.listdir(folder)
    #print '\n'.join(things)
    for o in m.objects:
        print o

