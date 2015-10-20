import pandas as pd
import re
from os import listdir
from os.path import isfile, join

class transactions_appender():

    def __init__(self,mypath):
        self.mypath=mypath

    def read_files(self):
        passfiles=[]
        onlyfiles = [ f for f in listdir(self.mypath) if isfile(join(self.mypath,f)) ]
        for files in onlyfiles:
            a=re.match(r'mts.*',files,flags=0)
            if a:
                #print a.group()
                passfiles.append(a.group())
        #print len(passfiles)
        self.appends(passfiles)

    def appends(self,allfiles):

        frame = pd.DataFrame()
        list_ = []
        for file_ in allfiles:
            print self.mypath+file_
            try:
                df = pd.read_csv(self.mypath+file_,index_col=None, header=None)
                list_.append(df)
            except Exception,e:
                print 'no value'

        frame = pd.concat(list_)
        #print frame
        out_file=frame.drop_duplicates().reset_index(drop=True)
        #print out_file
        out_file.to_csv(self.mypath+'results/mts_active.csv',header=False,index=False)

if __name__=='__main__':
    myobj=transactions_appender('/home/tapas/mts/')
    myobj.read_files()
    print 'done!!'

